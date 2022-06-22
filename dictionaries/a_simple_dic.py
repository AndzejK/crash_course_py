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

# adding the coordination of the alien on a screen, the goal is to add a new key-value pair to the existing dictionary
alien_0["x_position"] = 0 
alien_0["y_position"] = 25
print(alien_0)

print(f"Still beginer coz the colour is {alien_0['colour']}")
# A user has progressed and colour has changed
alien_0["colour"] = "yellow"
print(f"The alien is now {alien_0['colour']}")

# let's move the alien 
print(f"The current alien's x-position: {alien_0['x_position']}")
# adding the speed param for the alien
alien_0["speed"] = "medium"

# Move the alien to the right.
# Determine how far to move alien based on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
#the new position is the old position plus the increment
alien_0["x_position"]=alien_0["x_position"]+x_increment
print(f"New alien's x-position: {alien_0['x_position']}")