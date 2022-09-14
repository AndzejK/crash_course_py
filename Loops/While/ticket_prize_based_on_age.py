#A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; 
# if they are between 3 and 12, the ticket is $10; and 
# if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and 
# then tell them the cost of their movie ticket.

prompt="How old are you: "
msg="The ticket cost is"
age=input(prompt)
age=int(age)
if age<3:
    print(f"{msg} free")
# between 3 and 12
elif 3<=age<12:
    # e.x. 3<=10<12
    print(f"{msg} $10")
else:
     print(f"{msg} $15")