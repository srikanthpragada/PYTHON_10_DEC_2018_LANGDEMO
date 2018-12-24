class MonthNames_Iterator:
    def __init__(self, names):
        self.pos = 0
        self.names = names

    def __next__(self):
        if self.pos == len(self.names):
            raise StopIteration
        else:
            self.pos += 1
            return self.names[self.pos - 1]


class MonthNames:
    names = ('Jan', 'Feb', 'Mar')

    def __iter__(self):
        return MonthNames_Iterator(MonthNames.names)


m = MonthNames()
mi1 = iter(m)
print(mi1.__next__())
print(mi1.__next__())

mi2 = iter(m)
print(mi2.__next__())

print(mi1.__next__())

for n in m:
    print(n)

