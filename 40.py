#program to demonstrate variable length arguments in function
def demo(*numbers):
    print("In demo function")
    for number in numbers:
        print(number)
a,b,c= 10,20,30
print("a=",a)
print("b=",b)
print("c=",c)
demo(a,b,c)
