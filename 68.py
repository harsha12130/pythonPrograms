#program to demonstrate Exception Handling

try:
    x=10
    name="KLU"
    demo=[10,20,3.5,"klu",40]
    a=10
    b=20
    print(x)
    print(name[2])
    print(demo[3])
    print(a/b)
except Exception as e:
    print(e)
    
