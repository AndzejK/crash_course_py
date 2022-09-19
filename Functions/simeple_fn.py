from datetime import datetime
import pytz
def make_a_new_line():
    #just empty space
    print("")
# call a new created function
make_a_new_line()
current_date_and_time=datetime.datetime.now() #local time
time_in_sydney=datetime.datetime.now(pytz.timezone("Australia/Sydney"))
print(current_date_and_time)
print(time_in_sydney)
make_a_new_line()