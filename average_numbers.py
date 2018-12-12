# Program to take numbers until 0 and display average of given numbers
total = 0
count = 0

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    total += num
    count += 1

print("Average = ", total // count)
