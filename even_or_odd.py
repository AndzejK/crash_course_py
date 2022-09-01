prompt="Just enter a number and I'll tell you if it is EVEN or ODD: "
msg_Even="the given number is EVEN"
msg_Odd="the given number is ODD"
number=input(prompt)
number=int(number)
if number%2 == 0:
    print(f"{number} - {msg_Even}")
else:
    print(f"{number} - {msg_Odd}")