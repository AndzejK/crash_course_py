import json
from pyexpat import features

# Eplore the sturture of data
file_name="Data_Visualisation/json/eq_1_day_m1.json"
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
print(mags)
print(lons)
print(lats)

