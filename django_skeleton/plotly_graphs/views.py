from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objs as go 
import chart_studio.plotly as py

# Create your views here.

def plotly_globe(request):
    data = dict(type="choropleth",
    #colorscale = "YlOrRd", #yellow-red-ish scale
    locations = ["AFG", "ALB", "DEU", "ESP", "CHL", "RUS", "ZAF", "BRA", "POL", "USA"],
    locationmode = "ISO-3",
    z = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
    text = ['Afghanistan', 'Albania', 'Germany', 'Spain', 'Chile', 'Russia', 'South Africa', 'Brazil', 'Poland', 'USA'],
    marker  = dict(line = dict(color = "rgb(255,255,255)", width=.5)),
    colorbar = {"title": "Reds and Yellows"})

    layout = dict(title="Globe of Colors", geo = dict(showframe=False, projection = {"type":"orthographic"}))
    choromap_globe = go.Figure(data=[data], layout=layout)
    plot_div = plot(choromap_globe, output_type='div')
    return render(request, "plotly_graphs/plotly-globe.html", context={'plot_div': plot_div})
