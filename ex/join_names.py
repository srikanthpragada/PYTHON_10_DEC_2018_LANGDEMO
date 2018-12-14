names = []  # Empty list

while True:
    name = input("Enter a name [end to stop] :")
    if name == 'end':
        break

    names.append(name)

print(" - ".join(sorted(names)))
