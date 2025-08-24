#program to deonstrate while loop with else statement

print("CASE 1")
n=int(input("Enter Range="))
i=1
while i<=n:
    print(i)
    i+=1
else:
    print("End of while loop")

print("CASE 2")
n=int(input("Enter Range="))
i=1
while i<=n:
    if(i%3==0):
        break
    else:
        print(i)
    i+=1
else:
    print("End of while loop")

