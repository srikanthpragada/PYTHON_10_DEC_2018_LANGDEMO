teldir = {}

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break
    mobile = input("Enter mobile number :")
    teldir[name] = mobile

# print in sorted order by name

for n,m in sorted(teldir.items()):
    print( f"{n:10s} {m}")


