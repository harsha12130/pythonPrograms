#program to check given number is Armstrong or not

n=int(input("Enter input="))
temp=n

sum=0
while n!=0:
    digit=n%10
    sum+=pow(digit,3)
    n=n//10

if temp==sum:
    print(temp,"is an Armstrong number")
else:
    print(temp,"is not an Armstrong number")
