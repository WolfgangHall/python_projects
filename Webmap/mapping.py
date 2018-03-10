# map visualizations
import folium
# data organization
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def colorize_elevation(elevation):
    '''Used to colorize map marker points based on elevation.'''
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

# adds circular markers for each volcano location
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker
        (location=[lt, ln],
            radius=6,
            popup=str(el) + 'm',
            fill=True,
            fill_color=colorize_elevation(el),
            color='grey',
            fill_opacity=0.7
            )
        )

fgp = folium.FeatureGroup(name="Population")

#  displays polygons separating countries
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red'}))




map.add_child(fgv)
map.add_child(fgp)

# must be added after the feature group is added as a child
map.add_child(folium.LayerControl())

map.save("Map1.html")
