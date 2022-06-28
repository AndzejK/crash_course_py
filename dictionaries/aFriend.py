friend={
    "first_name":"Oliver",
    "last_name":"Lee",
    "age":40,
}
#printing each piece of info
print(f"{friend}")

fav_numbers = {
    "Mikie":3,
    "Oliver":8,
    "Mirka":7,
    "Brodie":3,
    "Andrew":10,
}

for key in fav_numbers:
    print(f"{key}'s favourite number is {fav_numbers[key]}")

#looping through a dic based on the book
for key,value in fav_numbers.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print("\n")

# adding a new array just with the name in order to find their favourite numbers
friends=["Andrew","Mirka"]
# print each name
for name in fav_numbers.keys(): # the dictionary
    print(f"Hey {name}")
# let's find out if I know their/friends favourite number
    if name in friends: # the List
        fav_number=fav_numbers[name]
        print(f"\tI see that your favourite number is {fav_number}")
    elif name not in fav_numbers.keys():
        print(f"Couldn't find the name: {name}")

# Looping through dictionary in a particular order 
for name in sorted(fav_numbers.keys()):
    print(name)

# get just values from the dictionaty
for number in fav_numbers.values():
    print(number)    

print("\n")
# let's extract just unique values/number from a dictionary, set => {}
for digit in set(fav_numbers.values()):
    print(digit)