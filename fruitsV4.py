# Declare variables 
LIST1 = {'Orange', 'Apple', 'Raspberry', 'Pear'}
LIST2 = {'Strawberry', 'Apple', 'Pear', 'Peach'}
SHAREDLIST = {}
UNIQUELIST = {}

# compare LIST1 and LIST2 and return as SHAREDLIST
SHAREDLIST = LIST1.intersection(LIST2)

# compare LIST1 and LIST2 and return unique as UNIQUELIST
UNIQUELIST = LIST1.symmetric_difference(LIST2)

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
