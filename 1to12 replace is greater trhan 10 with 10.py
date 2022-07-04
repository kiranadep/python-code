l = []
n = int(input("Number of elements in list=")) 
for i in range(0, n) :
           ele = int(input("enter element = ")) 
           l.append(ele) 
for i in range(0, n) :
           if(l[i] > 10) :
                    l[i] = 10
print(l)