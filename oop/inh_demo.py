class A:
    def process(self):
        print("Process of A")

    def print(self):
        print("In Class A")  # Call to built-in print()


class B(A):

    def process(self):  # Overriding
        A.process(self)
        super().process()
        print("Process of B")

    def calculate(self):
        print("Calculate of B")

class C(B):
    def calculate(self):
        print("Calculate of C")


obj = C()
obj.process()
obj.calculate()
obj.print()

