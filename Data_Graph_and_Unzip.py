import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.tools as tls
import plotly.graph_objs as go
#import random
import jsonReader
#import ipywidgets as widgets
#values is the input that DCK will input from the JSON file


def mean(vals):
    sum = 0
    for i in range(len(vals)):
        sum += vals[i]
    return sum/len(vals)





"""
What follows is a ckassical linear approximation of a good trendline, using the method
of least squares as presentedin the textbook Uncertainities and their Measurements
by Ifan Hugh and Thomas Hase, page 74
"""


def delta(vals):
    return len(vals)*sum(mult_tup(vals, vals)) - (sum(vals))**2


def intercept(valx, valy):
    return (sum(mult_tup(valx, valx))*sum(valy)-sum(valx)*sum(mult_tup(valx, valy)))/delta(valx)

def mult_tup(x, y):
    m = np.zeros(len(x))
    for i in range(len(x)):
        m[i] = x[i]*y[i]
    return m


def gradient(valx, valy):
    """print(valx)
    print(valy)
    print(summ(valx*valy))
    print(delta)"""
    return (len(valx)*sum(mult_tup(valx, valy))-sum(valx)*sum(valy))/delta(valx)

def fin_func(varXName, varYName):
    #make values by calling
    values = jsonReader.getDataCollection(varXName, varYName)

    xuser = (0, 0) #varXName
    yuser = (0,0) #varYName
    x, y = zip(*values)  # splits the tuples in values into two lists, x and y

    trial_array = np.linspace(0,max(x))
    super_array = np.linspace(0,max(x))
    for i in range(len(trial_array)):
        super_array[i] = trial_array[i]*gradient(x, y) + intercept(x, y)

    fig, ax = plt.subplots()
    ax.plot(trial_array, super_array)
    ax.scatter(x, y)
    ax.scatter(xuser, yuser)


    layout = go.Layout(
        title = "Plot of:\n" + str(varXName)+ " against \n" + str(varYName),
        xaxis = dict(
            title = str(varXName),
            titlefont=dict(
                family = 'Oswald, monospace',
                size = 18
             ),
        ),
        yaxis = dict(
            title=str(varYName),
            titlefont=dict(
                family='Oswald, monospace',
                size=18
        )
    )

    )
    trace1 = go.Scatter(x=x, y=y,  mode = "markers",  name = str(varXName) + " and " + str(varYName))
    #trace2 = go.Scatter(x=xuser, y=yuser, mode = "markers")
    trace3 = go.Scatter(x = trial_array, y = super_array, name = "Linear Correlation Line")
    data = [trace1, trace3]# trace3]
    plotly_fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(plotly_fig, show_link = False, filename='basic-scatter-plot.html',)
    with open('basic-scatter-plot.html', 'r') as myfile:
        html_words = myfile.read().replace("\n", '')
    print(html_words)

    return html_words




