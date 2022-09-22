def make_shirts(size,msg=""):
    if size.upper()=="L" and msg=="":
        msg="I love python"
    elif size.upper()=="M" and msg=="":
        msg="I love python"
    print(f"\nThe selected size: {size.upper()}")
    print(f"Your message on the T-shirt will be: {msg}")
#calling this fn using positional arg
make_shirts("S","I'm a coder")
#calling this fn using keyword arguments
make_shirts(size="m",msg="Love it!!")