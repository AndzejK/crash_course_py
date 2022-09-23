def get_formatted_full_name(name,lastName):
    person={"Name":name,"Surname":lastName}
    return person

coder=get_formatted_full_name("Andrew","Krupoves")
print(coder)

# Another option how I can an optional agument

def user_basic_info(name,surname,age=None):
    user_info={"Name:":name.title(),"Surname":surname.title()}
    if age:
        user_info["Age"]=age
    return user_info

coder_1a=user_basic_info("Mattew","smith",20)
coder_1=user_basic_info("Mattew","smith")
print(coder_1a)
print(coder_1)