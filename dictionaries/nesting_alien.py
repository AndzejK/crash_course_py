alien_0 = {
    "color":"white",
    "points":5,
}
alien_1 = {
    "color":"black",
    "points":10,
}
alien_2 = {
    "color":"green",
    "points":15,
}

# Storing dictionaries in a list
aliens = [alien_0,alien_1,alien_2]

# Getting & printing each dictionary stored in the list aliens
for alien in aliens:
    print(alien)
print("\n")

# let's create automatically aliens, 30 of them and store it in the list
aliens=[]
for alien_num in range(30):
    new_alien = {
        "color":"green",
        "points":15,
        "speed":"slow",
    }
    aliens.append(new_alien)

# Print the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Print total number of aliens
print(f"Total number of the aleins: {len(aliens)}")
print("\n")

# The game has progressed and it's time to update first three aleins to the next lvl
for alein in aliens[:3]:
    if alein["color"] == "green":
        # the order doesn't matter
        alein["points"]=20
        alein["speed"]="medium"
        alein["color"]="yellow"

for alien in aliens[:5]:
    print(alien)
print("...")
# Print total number of aliens
print(f"Total number of the aleins: {len(aliens)}")