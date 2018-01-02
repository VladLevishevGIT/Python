import folium
import pandas

map = folium.Map(location=[40.402, -3.904], zoom_start=3, tiles="Mapbox Bright")

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_generator(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], fill=True, fill_color=color_generator(el),
                                     radius=4, color=color_generator(el), popup=folium.Popup(str(el)+' m'), fill_opacity=1))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else
                            'orange' if x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map.html")