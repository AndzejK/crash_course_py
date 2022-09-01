# Write a program that asks the user what kind of rental car they would like. 
# Print a message about that car, such as “Let me see if I can find you a Subaru.
import re
prompt_msg="What kind of rental car you'd like: "
gen_msg="Let me see if I can find you "
asked_car=input(prompt_msg)
# Make sure if an article is correct
reg= re.findall("\A[aeiouyAEIOUY]",asked_car)
if len(reg)>=1:
    print(f"{gen_msg}an {asked_car}")
else:
     print(f"{gen_msg}a {asked_car}")
