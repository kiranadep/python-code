list1 = []
n = int(input("Enter no. of elements in list = "))
for i in range(0,n):
    ele = int(input("Enter element = "))
    list1.append(ele)
for i in range(0,n):
    print(list1[i]," is ",list1.count(list1[i]),"times in the list")