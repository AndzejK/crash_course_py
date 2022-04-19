from audioop import reverse

countries_to_visit=["Bali","Canada","Portugal","Chili","Brasil"]
print(countries_to_visit)
print(sorted(countries_to_visit))
print(countries_to_visit)
#Using sorted function to print temporarily list in reverse order
print(sorted(countries_to_visit,reverse=True))
print(countries_to_visit)
#Reverse the order permanently 
countries_to_visit.reverse()
print(countries_to_visit)
#Return the order back
countries_to_visit.reverse()
print(countries_to_visit)
countries_to_visit.sort()
#Sorting the list in alphabatic order, permanently, using sort() method
print(countries_to_visit)
#Sorting the list in reversed order, permanently, using sort() method
countries_to_visit.sort(reverse=True)
print(countries_to_visit)
