# Classify marks into grades: A (≥90), B (≥75), C (≥50), F (<50).

marks = int(input("Enter the marks of student :"))

if marks >=90 and marks<100:
    print("A Grade")
elif marks >=75 and marks<89:
    print("B Grade")
elif marks>=50 and marks<74:
    print("C Grade")
elif marks>=1 and marks<50:
    print("D Grade")
else:
    print("Put the marks between 1 to 100.")

'''
o/p
Enter the marks of student :95
A Grade

Enter the marks of student :82
B Grade

Enter the marks of student :64
C Grade

Enter the marks of student :45
D Grade

Enter the marks of student :150
Put the marks between 1 to 100.
'''

