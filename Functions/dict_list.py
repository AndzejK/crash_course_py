def greet_users(names):
    for name in names:
        msg=f"Hello, {name.title()}"
        print(msg)

users=["test1","TesT2","tEST3","test4","TesT5","tEST6"]

greet_users(users)

# Printing 3D company
unprinted_logos_1=['Top G','Coding for Life','Living my lif','I love Australia' ]
printed_logos_1=[]
'''
while unprinted_logos:
    current_logo=unprinted_logos.pop()
    print("Printing log: " + current_logo)
    printed_logos.append(current_logo)

#Display all printed logos
print("\nPrinted logos")
for printed_logo in printed_logos:
    print(f"{printed_logo}")
'''
#function which modifies/removes logos
def print_logos(unprinted_logos,printed_logos):
    while unprinted_logos:
            current_logo=unprinted_logos.pop()
            print("Printing log: " + current_logo)
            printed_logos.append(current_logo)
        
#function whcih printis array/logos
def show_printed_logos(printed_logos):
    print("\nPrinted logos")
    for printed_logo in printed_logos:
       print(f"{printed_logo}")

#calling this functions
print_logos(unprinted_logos_1,printed_logos_1)
show_printed_logos(printed_logos_1)