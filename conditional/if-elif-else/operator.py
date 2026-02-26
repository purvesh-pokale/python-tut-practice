# Input two numbers and an operator (+, -, *, /). Use if-elif to perform the correct operation.

n1 = int(input("Enter the 1st number :"))
n2 = int(input("Enter the 2nd number :"))

operator = input("Enter the opertor :")

if operator == '+':
    print("Addition :",n1+n2)
elif operator == '-':
    if n1<n2:
        n1,n2=n2,n1
        print("Subtraction :",n1-n2)
    else:
        print("Subtraction :",n1-n2)
elif operator == '*':
    print("Multiplication :",n1*n2)
elif operator == '/':
    print("Division :",n1/n1)
else:
    print("invild operator.")

'''
Enter the 1st number :5
Enter the 2nd number :5
Enter the opertor :*
Multiplication : 25

Enter the 1st number :5
Enter the 2nd number :5
Enter the opertor :+
Addition : 10

Enter the 1st number :5
Enter the 2nd number :5
Enter the opertor :-
Subtraction : 0

Enter the 1st number :2
Enter the 2nd number :5
Enter the opertor :-
Subtraction : 3

Enter the 1st number :10
Enter the 2nd number :5
Enter the opertor :/
Division : 1.0
'''
