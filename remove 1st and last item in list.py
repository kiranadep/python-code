l=[]
n = int(input('Enter number of elements=')) 
for i in range(0,n):
    ele = int(input("enter element= "))
    l.append(ele)
l.pop(0)
l.pop(-1)
l.sort()
print("After removing first and last item, and by sort:",l)