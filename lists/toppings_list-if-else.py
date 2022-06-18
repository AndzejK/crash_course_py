toppings=["Artichoke hearts","Portobello","Camembert","BBQ Chicken","Pecans"]
#go through all toppings
for topping in toppings:
#print that of the toppings is not available
    if topping=="Camembert":
        print(f"Sorry, but {topping} isn't available at the moment")
#print adding a topping from the list
    else:
        print(f"Adding {topping}")
#announcing that the task has been completed 
print("\nPizza has been made!")