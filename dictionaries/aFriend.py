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