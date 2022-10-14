import csv
from fileinput import filename
filename='/Users/rock/Documents/scripts/python/python_crash_course/Data_Visualisation/sitka_tem.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)