import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
dictionary = {
    'A' : [12, 14.8, 16, 20],
    'B' : [1]

}
N = 2
dictionary_names = [i for i in dictionary]
c = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]

"""data = [{
    'y': dictionary[dictionary_names[i]],
    'name': dictionary_names[i],
    'type': 'box',
    'marker':{'color': c[i]}} for i in range (2)
]"""
data = []
for i in range(len(dictionary)):
    data.append(go.Box(
        y=dictionary[dictionary_names[i]],
        name=dictionary_names[i],
        boxpoints = 'all',
        marker=dict( size=2,),
        line=dict(width=1),

    ))




py.iplot(data, filename = 'maymays.html')


