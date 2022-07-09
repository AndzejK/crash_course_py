#people
tom = {
    "name":"tom",
    "surname":"smykowski",
    "occupation":"Senior Full-Stack Software Developer",
    "education":"Uniwersytet Kazimierza Wielkiego",
}
andrew = {
    "name":"andrew",
    "surname":"sterkowitz",
    "occupation":"Software Developer",
    "education":"DeVry University",
}
david = {
    "name":"david",
    "surname":"bombal",
    "occupation":"YouTuber",
    "education":"unknown",
}
#storing info about each person in the list
people = [tom,andrew,david]
#print eveything I know of each another
print(f"All info what I've got:")
for person in people:
    for key,value in person.items():
        print(f"{key.title()}: {value.title()}")
    print("\n")
