# If I want to change/modify a list is better off using while loop, mmm
## Let's assume we have a list where are uncomfirmed_users that needs to be verified and 
## and located to another list, confimed_users

unconfirmed_users=["Andrew","brodie","mikie","cris"]
confirmed_users=[]
# while I'm not empty I'm gonna do what u r telling me
while unconfirmed_users:
    # create a new var to store a value from a list
    # pop() - takes the last user for the list
    current_user=unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    # append() - just adds a value in row
    confirmed_users.append(current_user)
# Display all confimed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

