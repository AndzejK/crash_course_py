# Here we need to make sure how we'd like to structure our fn, since we can have positional or keyword based arguments
# If positional, in out case as a pet type a dog is common then we place as a last argm and fisrt as a nme

def describe_a_pet(pet_name, pet_type="dog"):
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")

describe_a_pet("roychik")

#chane default value just add in th fn what you want to
# here we use keyword aguments what makes our life easier 
describe_a_pet(pet_type="fish",pet_name="Emo")