# Declare variables 
LIST1 = {'Orange', 'Apple', 'Raspberry', 'Pear'}
LIST2 = {'Strawberry', 'Apple', 'Pear', 'Peach'}
SHAREDLIST = {}

# loop to print the content of LIST1 on new lines
print("List 1 Content")
print("**************")
for i in LIST1:
    print(i)
print("**************")
print("")

# loop to print the content of LIST2 on new lines
print("List 2 Content")
print("**************")
for i in LIST2:
    print(i)
print("**************")
print("")

# compare LIST1 and LIST2 and return as SHAREDLIST
SHAREDLIST = LIST1.intersection(LIST2)

# loop to print the content of SHAREDLIST on new lines
print("Cross over of both Lists")
print("************************")
for i in SHAREDLIST:
    print(i)
print("************************")
