# Keyword arguments it is just name value pair where I describe name of variable and its value
def describe_a_pet(pet_type,pet_name):
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")

#The difference is that I don't need to worry about the args positionig when I CALL the fn
describe_a_pet(pet_name="roychik",pet_type="dog")