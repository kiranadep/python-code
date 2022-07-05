n = int(input("Enter number of process :"))
BT = []
WT = []
TAT = []
w = 0
a = 0
for i in range(n):
    a = int(input(f"process[{i+1}] :"))
    BT.append(a)

WT = BT.copy()
WT.insert(0, 0)
for i in range(1, n):

    WT[i] = WT[i-1]+BT[i-1]


WT.insert(n,0)
TAT = BT.copy()
print("BT\tWT\tTAT")
for i in range(0,n):

    TAT[i] = WT[i]+BT[i]
    print(BT[i], "\t", WT[i], "\t", TAT[i])
   
for i in range(n):
    w += WT[i]
    a += TAT[i]

print(a)
w = w / n
a = a / n

print("The Average of WT is :", w, "\nThe Average of TAT is :", a)
