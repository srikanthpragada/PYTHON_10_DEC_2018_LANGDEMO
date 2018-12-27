FILENAME = r"e:\classroom\python\dec10\names.txt"

names = []
while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break
    names.append(name)

with open(FILENAME,"wt") as f:
    for name in sorted(names):
        f.write(name + "\n")

