responses = {}
# Set the flag that the pool is active
pooling_active=True # active
while pooling_active:
    # Use a name as a key and response as a value
    name = input("\nWhat's your name: ")
    response = input("Which country you would like to visit someday: ")
    # time to store the data in responses dic
    responses[name]=response
    # Ask if an user wants to add more members
    repeat = input("Do you know SB who wants to partcipate in this nonse? (yes / no) ")
    if repeat=="no".lower():
        pooling_active=False
    # we're done with pooling and let's display the results
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(f"{name.title()} would like to go to {response.title()}")
