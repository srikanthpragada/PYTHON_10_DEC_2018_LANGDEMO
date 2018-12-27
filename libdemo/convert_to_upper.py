FILENAME = r"e:\classroom\python\dec10\names.txt"

with open(FILENAME, "rt") as f:
    names = f.readlines()

with open(FILENAME, "wt") as f:
    for n in names:
        f.write(n.upper())
