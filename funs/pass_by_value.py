def fun(n):
    print("Before change ", id(n))
    n = 100
    print("After change ", id(n))

def add_zero(lst):
    lst.append(0)

v = 10
print(id(v))
fun(v)
print(id(v))
print(v)

nums = [1,2,3]
add_zero(nums)
print(nums)

