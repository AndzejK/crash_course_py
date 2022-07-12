import math
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

set_of_numbers=range(50)
list_of_number=[]
for number in set_of_numbers:
    list_of_number.append(number)

multiple_numbers=[]
for number_in_the_list in list_of_number:
    if number_in_the_list%3 == 0:
        multiple_numbers.append(number_in_the_list)
    elif number_in_the_list%5 == 0:
        multiple_numbers.append(number_in_the_list)
print(multiple_numbers)
sum_=0
for sum in multiple_numbers:
    sum_+=sum
print(sum_)

number_xxx=range(3)
output={*number_xxx}
print(output)
