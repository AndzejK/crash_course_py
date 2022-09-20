from datetime import datetime
from pytz import timezone

#More info about strtime https://strftime.org/

# getting time in Vilnius LT
tz_vilnius=timezone("Europe/Vilnius")
tz_vilnius_cur_date=datetime.now(tz_vilnius).strftime("%Y/%m/%d")

#plain number for calculation
tz_vilnius_cur_date_number=datetime.now(tz_vilnius).strftime("%Y%m")

#print(tz_vilnius_cur_date)
tz_vilnius_cur_time=datetime.now(tz_vilnius).strftime("%I:%M %p")
print(tz_vilnius_cur_time)

# getting time in Sydney AU
tz_sydney=timezone("Australia/Sydney")
tz_sydney_cur_date=datetime.now(tz_sydney).strftime("%Y/%m/%d")
#print(tz_sydney_cur_date)
tz_sydney_cur_time=datetime.now(tz_sydney).strftime("%I:%M %p")

#plain number for calculation
tz_sydney_cur_time_number=datetime.now(tz_sydney).strftime("%I%M")
print(tz_sydney_cur_time)

# count difference between time zones Vilnius and Sydney
time_delta=tz_sydney_cur_date-tz_vilnius_cur_time
print(time_delta)