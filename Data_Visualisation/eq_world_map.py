import json
from tkinter.tix import Tree
from turtle import title
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Eplore the sturture of data
    # Data_Visualisation/json/all_earthquakes.json
    # Data_Visualisation/json/eq_1_day_m1.json
file_name="Data_Visualisation/json/M1_30_days_earthquakes_Real.json"
with open(file_name) as f:
    all_eq_data=json.load(f)
all_eq_dicts=all_eq_data["features"]

# Extracting magnitudes from JSON
mags,lons,lats, hover_texts=[],[],[],[]
for eq_dic in all_eq_dicts:
    mag=eq_dic["properties"]["mag"]
    lon=eq_dic["geometry"]["coordinates"][0]
    lat=eq_dic["geometry"]["coordinates"][1]
    title_=eq_dic["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title_)

# Map the Earthquicks and their severity
data=[{
    "type":"scattergeo",
    "lon":lons,
    "lat":lats,
    "text":hover_texts,
    "marker":{
        "size": [5*mag for mag in mags],
        "color":mags,
        "colorscale":'Cividis',
        "reversescale": True,
        "colorbar":{"title":'Magnitude'}
    },
}]

my_layout=Layout(title="Global Eathquakes")

fig={"data":data,"layout":my_layout}
offline.plot(fig,filename="global_earthquakes.html")