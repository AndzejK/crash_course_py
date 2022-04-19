pizzas=["Pepperoni","Barbeque","Hawaiian","Alfredo","Margherita"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("To be honest, I don't like that much even pizza")

#copy the list of pizzas
friend_pizzas=pizzas[:]
#Addning a new pizza to the pizzas list
pizzas.append("Melted Cheese")
#Addning a new pizza to the friend_pizzas list
friend_pizzas.append("Tuscany Courtyard")
#Proving that we have the different lists 
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza}")
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
     print(f"\t{pizza}")

