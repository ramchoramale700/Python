def lists():
    list1=[]
    list2=[]
    print("Enter no:")
    for i in range(8):
         num=int (input(f"Enter number list1 {i+1}:"))
         num*=4
         list1.append(num)
         num2=int(input(f"Enter number for list2 {i+1}:"))
         num2*=2
         list2.append(num2)
    print("After Multiply by 4 list 1: ",list1)
    print("After Multiply by 2 list 2:",list2)
lists()