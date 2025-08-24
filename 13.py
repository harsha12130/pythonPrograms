#program to display large number among three numbers using elif ladder
a=int(input("Enter first number"))
b=int(input("Enter Second number"))
c=int(input("Enter Third number"))
if a>b and a>c:
    print(a,"is Big number")
elif b>c:
    print(b,"is Big number")
else:
    print(c,"is Big number")
