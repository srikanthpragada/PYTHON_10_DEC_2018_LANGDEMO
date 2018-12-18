def iseven(n):
    return n % 2 == 0


def abs(n):
    return n if n >= 0 else n * -1


nums = [10, 11, 22, 30, 45, 55]
for n in filter(iseven, nums):   # iseven(n) : boolean
    print(n, end=' ')
print("\n")
nums = [-10, 11, -22, 30, 45, 55]
for n in sorted(nums):
    print(n, end=' ')

print("\nSorted By Abs Value\n")

for n in sorted(nums, key=abs):  # abs(n) : number
    print(n, end=' ')
