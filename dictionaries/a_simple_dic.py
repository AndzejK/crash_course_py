# A dictionaries in python it is a way to store a bunch of info wich is attached to some value,
# Or DICT is a collection of key-value pairs

# a game that is featuring alines
alien_0={"colour": "green", "points":5} 

#gaining access to the values in dictionary
print(alien_0["colour"])
print(alien_0["points"])

#let's say a player shoot down this alien
new_points=alien_0["points"]
print(f"You just earned {new_points} points")