g = 1000


def fun1():  # Enclosing function
    global g
    v1 = 10
    ev = 100
    g = 100
    print("In fun1()", v1)

    def fun2():  # Local function
        nonlocal v1
        v1 = v1 + 1
        v2 = 20
        print("In fun2()", g, ev, v1, v2)

    fun2()
    print("End of fun1()", v1)


fun1()  # Module-level or global
print(g)