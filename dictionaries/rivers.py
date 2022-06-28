rivers = {
    "amazon":"brazil",
    "ganges":"india",
    "mississippi":"north america",
}

# Looping through dictionary
for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

# List just the rivers in the dictionary
for river in rivers.keys():
    print(river.title())
print("\n")
# List just the countries in the dictionary
for country in rivers.values():
    print(country.title())