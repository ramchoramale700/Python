list=[3,8,7,5,1,9,10]

for n in list:
    if n>1:
        for i in range(2,n):
            if n%i==0:
             break
        else:
            print(n,"is prime")