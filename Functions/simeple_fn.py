#was fucking around why the fuck fucking PYTZ wasn't working who fuck knows but then I changed my
# python version it starte working 
from datetime import datetime
import pytz
def make_a_new_line():
    #just empty space
    print("")
# call a new created function
make_a_new_line()
current_date_and_time=datetime.now() #local time
time_in_sydney=datetime.now(pytz.timezone("Australia/Sydney"))
print(current_date_and_time)
print(time_in_sydney)
make_a_new_line()