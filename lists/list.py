#List is a collection of items in a specific order, an order comes from Index side. 
countries=["australia","canada","lithuania","bali"]

#in order to return ALWAYS LAST item from the list use -1!
print(countries[-1].title())

#Using the logic above if I want to return an item before the LAST item/ the 2nd item from the END -2 and so on;
print(countries[-2].title())
print(countries[-3].title())
# 0 1st item
#-1 Last item
#  - - - - -  0 - - - - -
# -5-4-3-2-1  _+1+2+3+4+5
# [1,2,3,4,5][1,2,3,4,5]
print(f"\nI'm currently based in {countries[-2].title()}\nShortly I'll live in {countries[0].title()}\n")

#Add(append) an item to the end of the list
countries.append("portugal")
#Insert an item into a specific place of the List
countries.insert(2,"poland")

#copy countries to the another list
countries_edited=countries.copy()
print(countries[-1].title())


#It means that it inserts an item in that places and shifts prior item forward 
print(countries)

#Delete/remove an item from the list use del statement
del countries[2]
print(countries)

#if I want to use a deleted item from the list use pop() method, if it's empty/hollow it will remove/store the last item from the list
curr_count=countries.pop(2)
print(f"\nI live in {curr_count.title()}\n") 
print(countries)

#If I want to remove an iteam by its value use a remove() methof
not_fan="canada"
countries.remove(not_fan)
print(countries)
print(f"\nI used like {not_fan.title()}")

#           ______Sorting Out the lists______           #
print(f"Countries before sorting out   {countries_edited}")
#Sorting the list in alphabetic order, the change has made permanently!!!
countries_edited.sort()
print(f"Countries after sorting out    {countries_edited}")
#Sorting the list in reverse order, the change has made permanently!!!
countries_edited.sort(reverse=True)
print(f"Countries in the reverse order {countries_edited}")
#In order to sort the list just temporarily I can use the function sorted({list}), the thing with reverse, reverse=True e.x. sorted(countries_to_visit,reverse=True)
print(sorted(countries_edited))
print(countries_edited)

#Finding the length of a List use len({list}) function  
length_of_countries=len(countries_edited)
print(f"How many countries on the list?\n{length_of_countries}")

#Unintentional error, out of rage list
print(countries[9])