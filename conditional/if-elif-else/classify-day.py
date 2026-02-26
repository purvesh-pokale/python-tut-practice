#5.  Classify a day number (1-7) into weekday or weekend.
num = int(input("Enter the number to check a day :"))

if  num==1 or num==2 or num==3 or num==4 or num==5:
    print("Weekday")
elif num==6 or num==7:
    print("Weekend")
else:
    print("Enter the valide number to check a day.")

'''
o/p

Enter the number to check a day :4 
Weekday

Enter the number to check a day :6
Weekend

Enter the number to check a day :10
Enter the valide number to check a day.
'''