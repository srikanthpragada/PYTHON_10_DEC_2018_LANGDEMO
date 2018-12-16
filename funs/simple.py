def fun():
    print("Having fun!")


def add(*,a, b):
    print(a + b)

# add(a=10,b=20)
# add(b=10,a=20)


def hello(*names,message="Hello"):
    for n in names:
        print(message,n)

def info(**details):
    print(details)


info(a=10,b=20,c=30,message ='hello')
info(mobile='393933', email='abc@gmail.com')