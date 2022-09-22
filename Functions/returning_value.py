from turtle import title


# Adding default parameter for a middle name as empty argumnet 
# Since mid_name is optinal we place it at the end
def get_formatted_full_name(name,lastName,mid_name=""):
    # Python iterprets TRUE if it is NON-emptry string,"  " --- FALSE - empty, ""
    if mid_name:
        full_name=f"{name} {mid_name} {lastName}"
    else:
        full_name=f"{name} {lastName}"
    return full_name.title()

team_leader=get_formatted_full_name("andrey","krUpOvEs")
print(team_leader)
coder_1=get_formatted_full_name(mid_name="john",name="mIROSLAv",lastName="KruPOVes")
print(coder_1)
# positional arguments,have to pay attention to their place all the time
coder_2=get_formatted_full_name("Jordan","MIchal","Hopkin")
print(coder_2)

