nums = [10, 11, 22, 30, 45, 55]
for n in filter(lambda n: n % 2 == 0, nums):  # iseven(n) : boolean
    print(n, end=' ')
print("\n")
nums = [-10, 11, -22, 30, 45, 55]
for n in sorted(nums):
    print(n, end=' ')

print("\nSorted By Abs Value\n")

for n in sorted(nums, key=lambda n: n if n >= 0 else n * -1):  # abs(n) : number
    print(n, end=' ')
