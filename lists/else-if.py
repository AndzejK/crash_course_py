from operator import indexOf


msg_allowed="You are old enough to vote!\nHave you registered to vote yet?"
msg_notallowed="Sorry, you are too young to vote\nPlease register to vote as soon as you turn 18!"
age=66
#just two scenarios - ELSE chain #2
if age>=18:
    print(msg_allowed)
else:
    print(msg_notallowed)
#else-if one of the ACTIONS will be execyted! - ELIF chain #3

#amusement park price-list
cost_free=0
cost_for_under_18=25
cost_for_above_18=40
if age<=4:
    print(f"Your admission cost is {cost_free}")
elif age<=18:
  print(f"Your admission cost is {cost_for_under_18}")
else:
    print(f"Your admission cost is {cost_for_above_18}")

#same example but done it differentely
if age<4:
    prise=0
elif age<18:
    prise=25
#for senior off
elif age>65:
    prise=10
else:
    prise=40
print(f"Your admission cost is {prise}")

#Testing multiple conditions, just bunch of IFs
countries_init=["au","lt","sg","pl","ca"]
if "au" in countries_init:
    indx=countries_init.index("au")
    print(f"\nflyfing to {countries_init[indx].upper()}")
if "lt" in countries_init:
    indx=countries_init.index("lt")
    print(f"born in {countries_init[indx].upper()}")
if "rus" in countries_init:
    indx=countries_init.index("rus")
    print(f" {countries_init[indx]}")
if "pl"in countries_init:
    indx=countries_init.index("pl")
    print(f"been to {countries_init[indx].upper()}")

print("\nI'm sceptical about my choice to come back to AU, since I'm afraid badly.")

