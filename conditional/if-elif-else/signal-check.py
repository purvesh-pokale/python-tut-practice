# Input color ("red", "yellow", "green") and print "Stop", "Get Ready", or "Go". Otherwise, print "Invalid Color"

color = input("Enter the traffic signal color:")

if color=="red":
    print("Stop")
elif color=="yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid Color")

'''
Enter the traffic signal color:red
Stop

Enter the traffic signal color:yellow
Get Ready

Enter the traffic signal color:green
Go
'''