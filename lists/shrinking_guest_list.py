from ast import mod
from copy import copy

#The original list whos is invited
guests=["Katie","Sam","Oli","Arthur","Kevin","Sarah","Ana","Aaron"]
#A simple message telling that a person isn't invited :(
msg_cancel=", unfortunately, I cannot invite just two people, since a dinner table won't arrive on time:("
msg_invited=", you are stil invited"
#The list who isn't invited, I start as an empty one
list_guests_canceled=[]
#I'm copying the original list in order to get initial names from the original list - guests
mod_list=guests.copy()
#looping through the original list
for i in guests:
    #Just two people are invited from the original list
    if len(mod_list)>2:  
        #a number/index of a person on the original list, for pop() method
        indx=mod_list.index(i)
        #Choosing/removing a person from the original list, and here the whole original list shifts
        cancled_guest=mod_list.pop(indx)
        #Adding/appeding that person to the list who isn't invited
        list_guests_canceled.append(cancled_guest)
        print(f"{i}"+msg_cancel)
    else:
            #Invitation for two people
            #print(f"{i}"+msg_invited)
        #delinting last two guest from the list of invited people    
        del mod_list[indx]
#print(f"List who cannot come {list_guests_canceled}"
#print(f"List who can come {mod_list}")
print(mod_list)
