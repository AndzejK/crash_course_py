# Repeat the app till I tell you stop
from email import message
prompt="Tell me what to repeat! "
prompt+="\nIf yo're bored enter 'stop' and I'll end this hell\n "
msg=input(prompt)
msg=""
while msg.lower() !='stop':
    msg=input(prompt)
# When we write/enter stop the progamm still repeat the msg, therefore we need an IF statement 
    if msg!='stop':
        print(msg)

