guests=["Katie","Sam","Oli","Arthur","Kevin","Sarah","Ana","Aaron"]
msg_upd_1="I've found a bigger table!\n"
#print(msg_upd_1)
guests.insert(0,"Andrew")
guests.insert(5,"Max")
guests.append("Sue")
for i in guests:
    print(f"Hey, {i}\n"+msg_upd_1)