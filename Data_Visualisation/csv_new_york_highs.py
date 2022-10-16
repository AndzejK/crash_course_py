import csv
from fileinput import filename
import imp
from shutil import which
import matplotlib.pyplot as plt
from datetime import datetime
# the data from https://www.ncdc.noaa.gov/cdo-web/
filename='Data_Visualisation/data_csv/new_york_weather_for_21year.csv'

# Pay attention that all code is written inside/tabbed in "with" fn
with open(filename,) as f:
    reader=csv.reader(f) # file
    header_row=next(reader)
   
    # Get dates and highs tempratures from a current file
    dates,highs = [],[]
    for row in reader:
        if row[5]=='': #if empty string ignore
            continue
        
        current_date=datetime.strptime(row[2],"%Y-%m-%d")
        high=float(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the high tempratures
plt.style.use("seaborn")
fig, ax=plt.subplots()
ax.plot(dates,highs,c='black')

# Format plot.
plt.title("Daily high temprature for the whole 2021 year",fontsize=20)
plt.xlabel("",fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temprature (C)",fontsize=14)
plt.tick_params(axis="both",which="major",labelsize=14)
plt.show()



#print(highs)
   #print(header_row)
"""
for index, column_header in enumerate(header_row):
    print(index,column_header)
"""
