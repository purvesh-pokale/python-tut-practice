'''
5. Check if a string starts and ends with the same character 
Question: You are given a string word = "radar". Write an if-else statement that: - 
 Prints "Same start and end" if the first and last characters of the string are the same. - Otherwise, prints "Different start and end".
'''
word = input("Enter the string to check start and :")
#word = "radar"
if word[0] == word[-1]:
    print("Same start and end")
else:
    print("Different start and end")

'''
Same start and end ----- for "radar

Enter the string to check start and :purvesh
Different start and end

Enter the string to check start and :nun
Same start and end
'''