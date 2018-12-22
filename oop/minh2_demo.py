class A:
    def m1(self):
        print("M1() of A")


class B(A):
    def m2(self):
        print("M2() of B")


class C(A):
    def m1(self):
        print("M1() of C")

    def m2(self):
        print("M2() of C")


# Multiple Inheritance
class D(B, C):
    pass


obj = D()
obj.m1()
print(D.__mro__)
