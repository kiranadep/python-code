list1 = []
list2 = []
for i in range(1,8):
    ele = i
    list1.append(ele)
for i in range(1,8):
    elem = i * i
    list2.append(elem)
d = dict(zip(list1,list2))
print("Mapped Dictionary = ",d)