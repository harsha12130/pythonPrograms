#program to display digits of a given number
n=int(input("Enter input="))

while n>0:
    digit=n%10
    print(digit,end=" ")
    n=n//10
