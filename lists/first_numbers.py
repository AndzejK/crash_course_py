#print numbers from 1 to 3 in a newlind
for num in range(1,4):
    print(num)
#Create a list and add numbers from 1 to 3
numbers = list(range(1,11))
print(numbers)
#To get even numbers I can use a pace/step
even_numbers=list(range(2,11,2))
print(even_numbers)
#Get the 1st ten square numbers
square_numbers=[]
for num in range(1,11):
    square_numbers.append(num**2) #raising to the second power
print(square_numbers)
#DYO list comprehensions, in a line write a function above
digits=[num**2 for num in range(1,3)]
print(f"list comprehensions: {digits}")
#Get sum of digits in the list
digits=list(range(0,10))
sume=0
for digit in digits:
    sume+=digit
print(sume)

#functions sum/min/max
print(f"sum: {sum(digits)}")
print(f"min: {min(digits)}")
print(f"max: {max(digits)}")

