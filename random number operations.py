#random numberr 1-100
import random
l = []
for i in range(0,20):
    l.append(random.randint(1,100))
print(l)
#avrage of elements
sum = 0
for i in range(0,20):
    sum = sum + l[i]
    
avg = sum / 20
print("Average = ",avg)

#largest and smallest value inthe list 
l.sort()
print("Lasrgest  number =",l[-1],"Smallest number =",l[0])
#largest 2nd and smallest 2nd value inthe list 

print("second Lasrgest number =",l[-2],"second Smallest number =",l[2])
#print the number of even numbers

counter=0
for i in range(0,20):
    if (l[i]%2==0):
        counter=counter+1
print("total even numbers are =",counter)

       
