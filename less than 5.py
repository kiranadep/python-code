l=[]
n = int(input('Enter number of elements=')) 
for i in range(0,n):
    ele = int(input("enter element= "))
    l.append(ele)
new_lst=[]
for item in l:
    if item < 5:
        new_lst.append(item)
print("Items less than '5' are:",new_lst)