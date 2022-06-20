#Created an empty list
numbers=[]
#Adding numbers from 1 to 10
for number in range(1,11):
    numbers.append(number)

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")