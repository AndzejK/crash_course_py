current_users=["sweet_kristy","kristy_honey","bubbly_snOwflake","Angelic.princess.kristy","fairy.princess.kristy","baby_kristy_butterfly"]
new_users=["rock","Angelic.princess.kristy","shimmer","bubbly_snowflake","blossom"]

#Make sure that current_users list is lowercase
current_users_lowcase=[user.lower()for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lowcase:
        print(f"This username {new_user} exists in our DB, please create a new one")
    else:
        print(f"The username {new_user} is available")