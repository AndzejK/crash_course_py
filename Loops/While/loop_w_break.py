prompt="\nPlease enter the countries that you have visited."
prompt+="\nWhen you're done, just enter 'quit': "

while True:
    city=input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}!")
