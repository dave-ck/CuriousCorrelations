import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.tools as tls
import random
#import ipywidgets as widgets
from IPython.display import display
#values is the input that DCK will input from the JSON file

l = 1
h = 100
xuser = 10
yuser = 100
values = [(random.randint(l, h), random.randint(l, h)) for k in range(1500)]
x, y = zip(*values) #splits the tuples in values into two lists, x and y

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


def summ(vals):
    summ = 0
    for i in range(len(vals)):
        summ += vals[i]
    return summ


def delta(vals):
    return len(vals)*summ(vals**2) - (summ(vals))**2


def intercept(valx, valy):
    return (summ(valx**2)*summ(valy)-summ(valx)*summ(valx*valy))/delta(valx)



def gradient(valx, valy):
    print(valx)
    print(valy)
    print(summ(valx*valy))
    print(delta)
    return (len(valx)*summ(valx*valy)-summ(valx)*summ(valy))/delta(valx)

trial_array = np.linspace(0, len(values))
super_array = np.linspace(0, len(values))
"""for i in range(len(trial_array)):
    super_array[i] = trial_array[i]*gradient(x, y) + intercept(x, y)

fig, ax = plt.subplots()
ax.plot(trial_array, super_array)
ax.scatter(x, y)
ax.scatter(xuser, yuser)
plotly_fig = tls.mpl_to_plotly(fig)

plotly.offline.plot(plotly_fig, filename='basic-scatter-plot.html')

"""