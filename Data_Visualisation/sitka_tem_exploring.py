import csv
from fileinput import filename
filename='/Users/rock/Documents/scripts/python/python_crash_course/Data_Visualisation/new_york_weather_for_21year.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)