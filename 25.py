#program to display 1 to n odd numbers using any loop
n=int(input("Enter number="))
i=1
while i<=n:
    if i%2!=0:
        print(i)
    i+=1
#for i in range(1,n+1):
    #if n%2!=0:
        #print(i)
