#program to demonstrate for loop with else statement

print("CASE 1")
n=int(input("Enter Range="))

for i in range(1,n+1):
    print(i)
else:
    print("End of for loop")

print("CASE 2")
n=int(input("Enter Range="))

for i in range(1,n+1):
    if(i%5==0):
        break
    else:
        print(i)
else:
    print("End of for loop")

