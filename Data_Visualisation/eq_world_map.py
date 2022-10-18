import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Eplore the sturture of data
    # Data_Visualisation/json/all_earthquakes.json
    # Data_Visualisation/json/eq_1_day_m1.json
file_name="Data_Visualisation/json/past_30_days_earthquakes_M1.json"
with open(file_name) as f:
    all_eq_data=json.load(f)
all_eq_dicts=all_eq_data["features"]

# Extracting magnitudes from JSON
mags,lons,lats=[],[],[]
for eq_dic in all_eq_dicts:
    mag=eq_dic["properties"]["mag"]
    lon=eq_dic["geometry"]["coordinates"][0]
    lat=eq_dic["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the Earthquicks
data=[Scattergeo(lon=lons,lat=lats)]
my_layout=Layout(title="Global Eathquakes")

fig={"data":data,"layout":my_layout}
offline.plot(fig,filename="global_earthquakes.html")