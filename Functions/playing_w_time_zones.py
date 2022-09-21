from datetime import datetime
from pytz import timezone

#More info about strtime https://strftime.org/
        #### Vilnius ###
# getting time in Vilnius LT
tz_vilnius=timezone("Europe/Vilnius")
tz_vilnius_cur_date=datetime.now(tz_vilnius).strftime("%Y/%m/%d")

#Hour and min of Vilnius current time
tz_vilnius_curr_hour=int(datetime.now(tz_vilnius).strftime("%I"))
tz_vilnius_curr_min=int(datetime.now(tz_vilnius).strftime("%M"))
#print(f"Vilnius - hours: {tz_vilnius_curr_hour} min: {tz_vilnius_curr_min}")

#Current time in Vilnius
tz_vilnius_cur_time=datetime.now(tz_vilnius).strftime("%I:%M %p")
print(f"\nVilnius: {tz_vilnius_cur_time}")

        ### Sydney ###

# getting time in Sydney AU
tz_sydney=timezone("Australia/Sydney")
tz_sydney_cur_date=datetime.now(tz_sydney).strftime("%Y/%m/%d")
#print(tz_sydney_cur_date)
tz_sydney_cur_time=datetime.now(tz_sydney).strftime("%I:%M %p")

#Current time in Sydney
tz_sydney_cur_time_number=datetime.now(tz_sydney).strftime("%I%M")
print(f"Sydney: {tz_sydney_cur_time}")

#Hour and min of Vilnius current time
tz_sydney_curr_hour=int(datetime.now(tz_sydney).strftime("%I"))
tz_sydney_curr_min=int(datetime.now(tz_sydney).strftime("%M"))
#print(f"Vilnius - hours: {tz_sydney_curr_hour} min: {tz_sydney_curr_min}")

# count difference between time zones Vilnius and Sydney
time_delta_hours=tz_sydney_curr_hour-tz_vilnius_curr_hour
time_delta_min=tz_sydney_curr_min-tz_vilnius_curr_min
print(f"Difference between Sydney and Vilnius is {time_delta_hours} hours\n")
