#program to display large number among three numbers using nested if else
a=int(input("Enter First number="))
b=int(input("Enter Second number="))
c=int(input("Enter Third number="))
if a>b:
    if a>c:
        print(a,"is a Big number")
    else:
        print(c,"is a Big number")
else:
    if b>c:
        print(b,"is a Big number")
    else:
        print(c,"is a Big number")
