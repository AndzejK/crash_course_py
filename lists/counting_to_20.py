#comprehensive list
digits=[num*1 for num in range(1,21)]
print(digits)

for num in range(1,21):
    print(num)
#A milion count
big_data=list(range(1,1_000_001))
#for digit in big_data:
#    print(digit)
min_big_data=min(big_data)
print(min_big_data)
max_big_data=max(big_data)
print(max_big_data)
sum_1=0
for i in big_data:
    sum_1+=i
print(sum_1)
sum_2=sum(big_data)
print(sum_2)
#find odd number from 1 to 20
odd_numbers=list(range(1,21,2))
for number in odd_numbers:
    print(number)
print("I'm done here")
#multiply by 3, from 3 to 30
mult_by_3=[num*3 for num in range(3,31)]
for j in mult_by_3:
    print(j)
print(len(mult_by_3))
print("I'm done with multiplying by 3 each number")
#The numbers raised to a cube
cube_numbers=[num**3 for num in range(1,11)]
for k in cube_numbers:
    print(k)
print(f"There are {len(cube_numbers)} digits in cube_numbers list ")