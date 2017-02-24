import plotly.plotly as py
from plotly.graph_objs import *

def draw(visits, n_games):

    layout = Layout(
    xaxis=dict(title='Square'),
    yaxis=dict(title='Percentage of visits')
    )
    trace0 = Bar(
        x=visits.keys(),
        y=visits.values()
    )
    data = Data([trace0])
    fig = Figure(data=data, layout=layout)
    py.plot(fig, filename = 'monopoly- {} games'.format(n_games))