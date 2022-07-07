# having a list in the dictionary

# Storing info someone's order
pizza_client_1={
    'crust':"thick",
    "toppings":["mushrooms","extra cheese"],
} 
# pritn info for the client, if it is correct info
print(f"You've ordered a {pizza_client_1['crust']}-crust pizza" 
    #breaking the line for better readability, just for a developer ;)
    " with the following toppings:")
for topping in pizza_client_1["toppings"]:
    print("\t" + topping+";")