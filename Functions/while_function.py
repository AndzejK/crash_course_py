def user_basic_info(name,surname,age=None):
    user_info={"Name:":name.title(),"Surname":surname.title()}
    if age:
        user_info["Age"]=age
    keys=[]
    values=[]
    for i in user_info:
        keys.append(i)
        values.append(user_info[i])
    return values

user1=user_basic_info("caif","cafe",20)
#print(user1[0])

while True:
    print("\nPlease tell me your name: ")
    print("enter 'q' at any time to quit.")
    f_name=input("First name: ")
    if f_name=="q":
        break
    f_surname=input("Surname: ")
    if f_surname=="q":
        break
    f_age=input("How old are you: ")
    if f_age=="q":
        break
get_names=user_basic_info(f_name,f_surname,f_age)
print(f"{get_names}")