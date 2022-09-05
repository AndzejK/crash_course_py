prompt="\nEnter your fav pizza topping."
prompt+="\nWhen you're done write - 'done': "
pizza_topping=""
while pizza_topping!="done":
    pizza_topping=input(prompt)
    if pizza_topping!="done":
        print(f"I'll add the {pizza_topping} topping")
    else:
        print("what was great choice, please come again!")
