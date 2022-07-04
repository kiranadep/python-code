def new_func():
    l1 =[]
    n1 = int(input("Enter how many values do you want :"))
    for i in range(n1):
        l1n1 = int(input(f"Enter value {i+1} :"))
        l1.append(l1n1)

    l2=[]
    n2 = int(input("Enter how many values do you want :"))
    for i in range(n2):
        l2n2 = int(input(f"Enter value {i+1} :"))
        l2.append(l2n2)
#l3 = list(set().union(l1,l2))
    l3 = list(set().union(l1,l2))
    print("the l1 and l2 of union is  :",l3)

new_func()