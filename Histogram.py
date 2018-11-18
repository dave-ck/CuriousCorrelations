#import matplotlib.pyplot as plt
import numpy as np
import plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
"""dictionary = {
    'A' : [12, 14.8, 16, 20],
    'B' : [1],
    'c' : [12, 2, 14, 10],
    'd' : [12, 2, 4, 5],
    '3' : [1, 3, 4, 5]

}"""

def plottingBox(dictionary):
    N = len(dictionary)
    dictionary_names = [i for i in dictionary]
    c = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]
    traces = [{
    'y': dictionary[dictionary_names[i]],
    'name': dictionary_names[i],
    'type': 'box',
    'marker': {'color':c[i]}


    } for i in range (int(N))]
    py.offline.plot(traces, filename = 'boxplot.html')
    with open('boxplot.html', 'r') as myfile:
        box_html = myfile.read().replace('\n', '')
    return box_html

"""fig, axs = plt.subplots(ncols = len(dictionary), sharey = True)
axs = axs.ravel()
for i in range(len(dictionary)):
    axs[i].boxplot(dictionary[dictionary_names[i]], vert = True)
plt.show()
plotly_fig = tls.mpl_to_plotly(fig)
plotly.offline.plot(plotly_fig, 'gay_shit.html')"""



