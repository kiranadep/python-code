l=[]
n = int(input('Enter number of elements=')) 
count=0
for i in range(0,n):
    ele = int(input("enter element= "))
    l.append(ele)
for i in range(0,len(l)):
    if(5==l[i]):
        count=count+1
print("Count of 5 is:",count)