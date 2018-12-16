teldir = {}

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break
    mobile = input("Enter mobile number :")
    if name in teldir:  # name exists, add number to existing set
       teldir[name].add(mobile)
    else:
       # new entry, add name and mobile as set
       teldir[name] = {mobile}


# print in sorted order by name

for name,numbers in sorted(teldir.items()):
    mobiles = ','.join(sorted(numbers))
    print( f"{name:10s} {mobiles}")


