f = open("file1.txt","r")
for line in f:
    txt = line.title()
    print(txt)
print("\n")
#Using try and except if file is not present
try:
    f1 = open("file2.txt","r")
except:
    print("File not found")
for line in f:
    txt = line.title()
    print(txt)
print("\n")
#Using capitalize()
f3 = open("file1.txt","r")
data = f3.read()
d1 = data.split()
for line in d1:
    l = line.capitalize()
    print(l)