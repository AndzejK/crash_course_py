                                    # creates an empty dir
                        # and accepts any num of key-value args -kwargs
def collecting_user_info(first,last,**user_info):
    user_info['first_name']=first.title()
    user_info['last_name']=last.title()
    return user_info

user_profile_1=collecting_user_info("andrey","perfect",age='30',title='client support specialist')
print(user_profile_1)