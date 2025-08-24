#program to display o to n even numbers using for loop
n=int(input("Enter number:"))
for i in range(n+1):
    if i%2==0:
        print(i)
