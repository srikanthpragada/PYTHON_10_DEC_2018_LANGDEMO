class A:
    def m1(self):
        print("M1() of A")


class B(A):
    def m1(self):
        print("M2() of B")


class C(B):
    pass

obj = C()
print(C.__mro__)
