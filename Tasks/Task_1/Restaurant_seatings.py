# Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

prompt="How many people are in their dinner group"
msg_1="Unfortunately, you have to wait for a table :("
msg_2="The table is ready"
num_of_people=input(prompt)
num_of_people=int(num_of_people)
if num_of_people>8:
    print(msg_1)
else:
    print(msg_2)
