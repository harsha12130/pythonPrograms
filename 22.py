#program to display n natural numbers in such a way that if the number is dvisible by 5 print KLU otherwise print number
n=int(input("Enter number="))
for i in range(1,n+1):
    if i%5==0:
        print("KLU")
    else:
        print(i)
