from pathlib import Path
import json
import plotly.express as px

# Step 1: Load the JSON data
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Step 2: Explore the data
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))  # Output: 160 (number of earthquakes recorded)

# Step 3: Extract magnitudes, latitudes, and longitudes
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10], lons[:10], lats[:10])

# Step 4: Plot the data on a world map
fig = px.scatter_geo(lat=lats, lon=lons, title='Global Earthquakes')
fig.show()
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, color=mags,
                     title='Global Earthquakes',
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth')
fig.show()

# Step 5: Add hover text with earthquake titles
eq_titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

fig = px.scatter_geo(lat=lats, lon=lons, size=mags, color=mags,
                     title='Global Earthquakes',
                     hover_name=eq_titles,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth')
fig.show()