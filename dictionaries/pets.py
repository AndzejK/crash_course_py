pet_1 = {
    "animal":"dog",
    "name":"roy",
    "breed":"rottweiler",
    "owner":"mirek",
}
pet_2 = {
    "animal":"bird",
    "name":"ambition",
    "breed":"cockatoo",
    "owner":"zoo", 
}
pet_3 = {
    "animal":"fish",
    "name":"miracle",
    "breed":"carp",
    "owner":"ocean", 
}
pets = [pet_1,pet_2,pet_3]
print(f"All info about pets:")
for pet in pets:
    for name,value in pet.items():
        print(f"\t{name.title()}: {value.title()}")
    print("\n")
