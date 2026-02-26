'''
Check if a string exists as a dictionary value
Question:
You are provided a dictionary inventory = {"item1": "chair", "item2": "table"} and a variable check = "chair".
 Write an if-else statement to check if the value of check exists anywhere in the dictionary.
- If it exists, print "Found in inventory".
- Otherwise, print "Not found".
'''

inventory = {"item1": "chair",
              "item2": "table"}


if "chair" in inventory.values():
    print("Found in inventory")
else:
    print("Not found")

#o/p: Found in inventory