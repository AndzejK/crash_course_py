#when we have a few list and want to do something with them
## Case in Pizzeria ##
available_toppings=["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese"]
requested_toppings=["mushrooms","french fries","extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Unfortunately, we don't have {requested_topping}")
print("\nPizza is ready\n")

# Case No.2 Print the names of users with some common text and if an user is Admin print special txt

users_list=["rock","soldier","Admin","sunflower","born_to_kill"]

for user in users_list:
    #removing all items from the list
    users_list.clear()
    if len(users_list)==0:
        print(f"We need to find some users!")
    elif user.lower()=="admin":
        print(f"Hello {user},would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")