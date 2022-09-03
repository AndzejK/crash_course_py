# FLAGS - a variable that determins While loop
prompt="Tell me what to repeat! "
prompt+="\nIf yo're bored enter 'stop' and I'll end this hell\n "
msg=input(prompt)
active=True
while active:
    msg=input(prompt)
    if msg=='stop':
        active=False
    else:
        print(msg)
