class MonthNames:
    names = ['Jan', 'Feb', 'Mar']

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if self.pos == len(MonthNames.names):
            raise StopIteration
        else:
            self.pos += 1
            return MonthNames.names[self.pos - 1]


m = MonthNames()
mi1 = iter(m)
print(mi1.__next__())
print(mi1.__next__())

mi2 = iter(m)
print(mi2.__next__())

print(mi1.__next__())
