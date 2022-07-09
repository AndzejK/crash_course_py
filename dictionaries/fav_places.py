favourite_places = {
    "andrey":{
        "place_1":"sydney",
        "place_2":"bali",
        "place_3":"thailand",
    },
    "dima":{
        "place_1":"canada",
        "place_2":"berlyn",
        "place_3":"amsterdam", 
    },
    "ahmed":{
        "place_1":"philippines",
        "place_2":"croatia",
        "place_3":"new york", 
    },
}
#get each name and its favourite places
for name,places in favourite_places.items():
    print(f"\t{name.title()}'s favourite places are:")
    #just getting values
    start=1
    for place in places.values():
        find_length=len(places.values())
        if start == len(places.values()):
            print(f"\t\t{place.title()}.")
        else:
            print(f"\t\t{place.title()};")
            start+=1
    print("\n")