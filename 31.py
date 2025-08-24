#program to display digits count, individual digits, sum of digits of a given number
n=int(input("Enter number:"))
count=0
sum=0

while n!=0:
    digit=n%10
    print(digit,end=" ")
    count=count+1
    sum=sum+digit
    n=n//10
print(end="\n")
print("Digits Count=",count)
print("Sum of Digits=",sum)
      
