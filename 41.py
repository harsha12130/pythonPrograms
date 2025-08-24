#progrsm to find factorial of a given number
def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
n=int(input("Enter Input:"))
print("Factorial of",n,":",fact(n))
