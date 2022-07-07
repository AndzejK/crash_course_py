# it can be a bir messy and complicated

from unicodedata import name


users = {
    "andzejk":{
        "name":"andzej",
        "surname":"krupovec",
        "location":"Bangkok",
    },
    "soldierofpeace":{
        "name":"andrew",
        "surname":"huberman",
        "location":"california"
    }
}

#1 accessing the key and values from dict
for user_name,user_info in users.items():
    print(f"\nUsername: {user_name}")
    # get full name
    full_name = user_info["name"].title()+" "+user_info["surname"].title()
    location=user_info["location"].title()
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")