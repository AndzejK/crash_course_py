#Ask the user for a number, and then report whether the number is a multiple of 10 or not.
prompt="Gimme a number: "
num=input(prompt)
num=int(num)
if num % 10 == 0:
    print(f"Number {num} is a multiple of 10")
else:
    print(f"Number {num} is NOT a multiple of 10")