in_lst=input("Enter a List = ")
lst=in_lst.split()
len = 0
def length(lst):
    global len
    if lst:
       len = len + 1
       length(lst[1:])
    return len
len = length(lst)
print("\n Inputed List =",lst)
print("The length of a list is", len)
