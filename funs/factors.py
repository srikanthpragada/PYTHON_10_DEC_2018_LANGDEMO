# Using command line arguments

import sys

if len(sys.argv) == 1:
    print('Missing number!')
    sys.exit(1)


num = int(sys.argv[1])
for i in range(2,num//2 + 1):
    if num % i == 0:
        print(i)

