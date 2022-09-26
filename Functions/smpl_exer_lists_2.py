# Sending Messages: Start with a copy of your program. 
# Write a function called send_messages() that prints each text message 
# and moves each message to a new list called sent_messages as it’s “printed. 
# After calling the function, print both of your lists to 
# make sure the messages were moved correctly.

msgs=["Keep pushing!","you're doing well!","remember this moment.","consistency is the key!"]
sent_messages=[]
def send_messages(messages):
    for msg in messages:
        print(f"This message was sent: {msg}")
        sent_messages.append(msg)

# Passig a copy of the list
send_messages(msgs[:])
print(f"\nOrignal messages:{msgs}")
print(f"\nSent_messages: {sent_messages}")


