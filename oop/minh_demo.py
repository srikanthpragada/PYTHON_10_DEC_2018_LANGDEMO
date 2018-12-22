class A:
    def process(self):
        print("Process of A")

    def calculate(self):
        print("Calculate of A")


class B:
    def process(self):
        print("Process of B")

    def print(self):
        print("Print of B")


# Multiple Inheritance
class C(B,A):
    def print(self):
        A.process(self)
        B.process(self)
        super().print()


obj = C()
print(C.__mro__)
