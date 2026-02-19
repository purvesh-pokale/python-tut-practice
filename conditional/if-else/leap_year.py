#Take a year and check if it is a leap year.
year=int(input("Enter the year :"))

if year % 400 == 0 or(year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("not leep year")

'''
o/p
Enter the year :254
not leep year

Enter the year :2028
Leap year
'''