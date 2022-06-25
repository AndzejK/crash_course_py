# Looping through an entire list, when I want to perfom the same/one action for many items in the list use FOR loop
#from turtle import st
#from zipfile import _ReadWriteBinaryMode


myGoals=["Sound as a native English Speaker", "be healthy and fit","doing meaningul work/bussiness","girlfriend/wife","financially independent","Having mindful community","a couple of friends"]
#list each goal
for goal in myGoals:
    num=myGoals.index(goal)
    print(f"{num+1}: {goal}")
    #\n - Newline
print("Thank You before hand, and enjoy the journey!")

#slicing list
#print last three my goals
print(myGoals[4:])
#print last three my goals
print(myGoals[-3:])
#print from 2 to 5 goals = in total print 5 goals from the list
print(myGoals[1:6])

print("My first three goals:")
for goal in myGoals[-3:]:
    print (f"\t{goal}")
    
#copy a list
backup_goals=myGoals[:]
print(backup_goals)
#I just made the second label to my goals, if I change sth in one of them this change will be made on myGoals and backup_goals_v2
backup_goals_v2=myGoals
print(backup_goals_v2)

random_num=4887
make_string_random_num=str(random_num)
digits_in_random_num=len(make_string_random_num)
random_num_sum=0
for digit in make_string_random_num:
    random_num_sum+=int(digit)**digits_in_random_num

if random_num_sum == random_num:
    print(f"\nTrue {random_num} is narcissistic")
else:
    print(f"\nFalse {random_num} is not narcissistic")
