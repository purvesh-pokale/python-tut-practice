#Take a number and check if it is a 3-digit number or not.

num = int(input("Enter the number :"))
length =len(str(num))
if length == 3:
    print("It is three digit number.")
else:
    print("It is not a therr digit number.")

'''
Enter the number :123
It is three digit number.


Enter the number :5000
It is not a therr digit number.
'''