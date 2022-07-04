str=str(input("Enter a Sentence To Find Frequency Of Word Appearing : "))
def word_count(str):
    count=dict()
    words=str.split(" ")
    for word in words:
        if word in count:
           count[word]+=1
        else:
             count[word]=1
    print("Dictinory Of Word = ",count)
    for key,value in count.items():
        print(f"Frequnce Of Word '{key}'is :{value}")
word_count(str)