#program to find global variable in function
c=30     #global variable
def demo1():
    a=10     #local variable
    print("In demo1 function")
    print("a=",a)
    c=40
    print("c=",c)
def demo2():
    b=20     #local variable
    print("In demo2 function")
    print("b=",b)
    print("c=",c)
demo1()
demo2()
