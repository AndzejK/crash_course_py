# Open and close a file
with open("pi_digits.txt") as file_object:
# Read file
    lines=file_object.read()
# Initiation of string
pi_string=""
# Go through lines and making as a string
for line in lines:
    pi_string+=line

ran_num=input("Enter any number: ")
if ran_num in pi_string:
    print(f"This num is PI - {ran_num}")
else:
    print(f"No luck for {ran_num}")


