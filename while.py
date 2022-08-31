from email import message


message=input("Tell me and tell you what you have told me: ")
print(message)
#breaking down prompt/instruction
prompt="If you tell us your email we would provide more details"
prompt+="What's your e-mail: "
email=input(prompt)
print(f"email:", email)

#a program checks if you can buy a beer 
instruc_1="How old are you: "
age=input(instruc_1)
age=int(age)

if age>=18:
    print("\nYou're good to go, but dunno if it's a good choice!")
else:
    print("\nHold your horses, young champ")    