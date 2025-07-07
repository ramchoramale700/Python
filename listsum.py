list=[3,8,7,5,1,9]
sum=8
for i in range(len(list)):
    for j in range (i+1,len(list)):
        if list[i]+list[j]==sum:
            print(list[i],"+",list[j],"=",sum)
            break