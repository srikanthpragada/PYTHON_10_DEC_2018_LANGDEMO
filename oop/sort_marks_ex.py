# Print marks in sorted order

marks = []
for i in range(1, 6):
    try:
        n = int(input("Enter marks : "))
        marks.append(n)
    except ValueError:
        print("Invalid number!")

for n in sorted(marks):
    print(n)
