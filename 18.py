#program to demonstrate break statements
n=int(input("Enter Range="))

for i in range(1,n+1):
    if i==4:
        break
    else:
        print(i)
