# Write a series of conditional tests. Print a statement describing each 
# test and your prediction for the results of each test.

coutry="australia"
print("Is country=='australia' I predict True")
print(coutry=="australia")
print("Is country == 'lithuana'? I predict False.")
print(coutry == 'lithuania')

# IN
countries =["australia","bali","canada","portugal"]
look_up_country=[]
look_up_country.append("australia" in countries) #True
look_up_country.append("lithuania" in countries) #False
print(look_up_country)

colours=["blue","red","black","white"]
print("green" in colours)
fav_colour="blue"
print(f"is my favorite colour == blue => True" )
print(fav_colour=="blue")
print(f"is my favorite colour == green => False" )
print(fav_colour=="green")

'''
More Conditional Tests: You don't have to limit the number of tests you create to ten. 
If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
Have at least one True and one False result for each of the following:
    +Tests for equality and inequality with strings
    +Tests using the lower() method
    +Numerical tests involving equality and inequality, greater than and less than, 
     greater than or equal to, and less than or equal to
    +Tests using the and keyword and the or keyword
    +Test whether an item is in a list
    +Test whether an item is not in a list
'''
#Tests for equality and inequality with strings
a="2+2=5"
b="2+2=4"
print(f"\nthe string in a var is equal to the string in b var? - False")
print(a==b)
print(f"the string in a var is NOT equal to the string in b var? - True")
print(a!=b)
#Tests using the lower() method
usr_name="RoCk"
print("\nIf this, rock user name exists in the DB: True")
print(usr_name.lower()=="rock")
#Numerical tests involving equality and inequality, greater than and less than, 
#greater than or equal to, and less than or equal to
print(f"\nNumerical tests:\n\tis true that 0=-0, my answer: True\n\tCorrect answer: {0==-0}")
print(f"\tis false that 1=-1, my answer: True\n\tCorrect answer: {1!=-1}")
print(f"\tis true that 2>1, my answer: True\n\tCorrect answer: {2>1}") # greater than
print(f"\tis true that 7<8, my answer: True\n\tCorrect answer: {7<8}") # less than
print(f"\tis true that 10>=11, my answer: False\n\tCorrect answer: {10>=11}") # greater than or equal to
print(f"\tis true that 10<=10, my answer: True\n\tCorrect answer: {10<=10}") # less than or equal to

