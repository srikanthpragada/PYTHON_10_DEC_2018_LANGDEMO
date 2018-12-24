# Print marks in sorted order

marks = []
for i in range(1,6):
    n = int(input("Enter marks : "))
    marks.append(n)


for n in sorted(marks):
    print(n)
