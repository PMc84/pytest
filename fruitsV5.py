# Declare variables 
LIST1 = {'Orange', 'Apple', 'Raspberry', 'Pear'}
LIST2 = {'Strawberry', 'Apple', 'Pear', 'Peach'}
SHAREDLIST = {}
UNIQUELIST = {}
LIST1LOWER = {}
LIST2LOWER = {}

LIST1LOWER = {fruits.lower() for fruits in LIST1}
LIST2LOWER = {fruits.lower() for fruits in LIST2}

# compare LIST1 and LIST2 and return as SHAREDLIST
SHAREDLIST = LIST1.intersection(LIST2)
SHAREDLISTLOWER = LIST1LOWER.intersection(LIST2LOWER)

# compare LIST1 and LIST2 and return unique as UNIQUELIST
UNIQUELIST = LIST1.symmetric_difference(LIST2)
UNIQUELISTLOWER = LIST1LOWER.symmetric_difference(LIST2LOWER)

# Function that prints set content, input as set name, description of set
def print_func(LIST, LISTNAME):
    # loop to print the content of LIST1 on new lines
    print(LISTNAME)
    print("**************")
    for i in LIST:
        print(i)
    print("**************")
    print("")

# Calling function for each list
print_func(LIST1, "List 1")
print_func(LIST2, "List 2")
print_func(SHAREDLIST, "Shared items")
print_func(UNIQUELIST, "Unique items")
print_func(LIST1LOWER, "Lower case list 1")
print_func(LIST2LOWER, "Lower case list 2")
print_func(SHAREDLISTLOWER, "Shared lower case items")
print_func(UNIQUELISTLOWER, "Unique lower case items")
