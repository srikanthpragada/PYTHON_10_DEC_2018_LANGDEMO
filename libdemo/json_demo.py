import json

class Person:
    def __init__(self,name,mobile):
        self.name = name
        self.mobile = mobile


p1 = Person("Abc","393939993")
js = json.dumps(p1.__dict__)   # dict to json
print(js)

p2 = json.loads(js)    # json to dict
print(type(p2), p2)



