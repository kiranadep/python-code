main_string = input("Enter the String = ")
sub_str = input("Enter the Sub-String = ")
if sub_str in main_string:
   print("Sub-string is present in string")
else:
    print("Sub-String is not present in string")
      
# using find()

main_string = input("Enter the String = ")
sub_str = input("Enter the Sub-String = ")
if ((main_string.find(sub_str)) == -1):
   print("Sub-string is not present in string")
else:
    print("Sub-String is present in string")
