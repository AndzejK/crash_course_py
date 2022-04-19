#Invited people
guests=["Katie","Sam","Oli","Arthur","Kevin"]
#Basic message 
greetings="Hey, "
msg="I'd would like you to invite for a dinner\n"
#List who can't make it
guest_canceled=[]
guest_canceled=guests.pop(2)
#List who can come instead of who can't make it
guests.insert(2,"Sarah")
#Print names and guests' names
print(greetings+guests[0]+"\n"+msg)
print(greetings+guests[1]+"\n"+msg)
print(greetings+guests[2]+"\n"+msg)
print(greetings+guests[3]+"\n"+msg)
print(greetings+guests[4]+"\n"+msg)
#Print who can't make it
print(f"Guests who can't make it:\n{guest_canceled}\n")
#Print who can come instead who can't make it
print(f"Instead of {guest_canceled} will be {guests[2]}")

