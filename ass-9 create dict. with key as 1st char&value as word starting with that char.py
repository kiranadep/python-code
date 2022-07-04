str=str(input("Enter a Sentence : "))
length=str.split()
dictinory={}
for word in length:
    
    if(word[0].lower()not in dictinory.keys()):
       dictinory[word[0].lower()]=[]
       dictinory[word[0].lower()].append(word)
else:
    
    if(word not in dictinory[word[0].lower()]):
       dictinory[word[0].lower()].append(word)
print("Dictionary = ",dictinory)
