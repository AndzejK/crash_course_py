#After IF keyword provided just list's name will check if the list got something
#True - when at least item is in there
#False - when is nothing in there
empty_list=[]
not_empty_list=["I'm not empty!"]
#1 Empty
if empty_list:
    print("looks like I got something!")
else:
    print("nothing in here, mate!\n")
#2 Not empty
if not_empty_list:
    print(f"looks like I got something!")
    for some in not_empty_list:
        print(f"\t{some}")
else:
    print("nothing in here, mate!\n")  