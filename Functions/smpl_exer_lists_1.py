# Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

msgs=["Keep pushing!","you're doing well!","remember this moment.","consistency is the key!"]

# Fn that excepts a list and just prints each value
def show_messages(list):
    for msg in list:
        print(msg.title())

show_messages(msgs)