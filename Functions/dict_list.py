def greet_users(names):
    for name in names:
        msg=f"Hello, {name.title()}"
        print(msg)

users=["test1","TesT2","tEST3","test4","TesT5","tEST6"]

greet_users(users)