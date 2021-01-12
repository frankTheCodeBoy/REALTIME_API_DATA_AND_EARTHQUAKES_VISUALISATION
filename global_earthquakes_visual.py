import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/30day_earthquake_data.json'
with open(filename) as f:
    all_eq_data = json.load(f)

chart_title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])
    
# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5.5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title=f"<b>\"{chart_title.upper()}.\"<b>")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='largescale_earthquakes.html')
