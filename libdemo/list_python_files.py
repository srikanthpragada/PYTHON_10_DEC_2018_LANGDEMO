import os


def print_file(filename):
    print(f"\nFilename : {filename}")
    print("-" * (len(filename) + 10))
    lineno = 1
    with open(filename, "r") as f:
        for line in f.readlines():
            print(f"{lineno:5d}: {line}", end='')
            lineno += 1


for dn, dirs, files in os.walk(r"e:\classroom\python\dec10\langdemo"):
    if dn.find('.git') >= 0 or dn.find('__py') >= 0:
        continue

    for f in files:
        if f.endswith('.py'):
            print_file(dn + "\\" + f)
