def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
n=int(input("Enter no:"))
print("factorial is :",fact(n))