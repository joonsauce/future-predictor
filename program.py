# number of items in dataset; if unknown, enter unknown
num_items = input("Enter the number of items in this set of data. If number of items is unknown, enter 'start': ")
# sets the list the data will go into
values = []
# check if num_items is a number
if not num_items == "start":
    # makes num_items an integer
    num_items = int(num_items)
    # adds in all the data from dataset into values
    for item in range(num_items):
        # sets some input to value
        value = input("Enter a value: ")
        # checks if value is a number
        if value.isnumeric():
            # adds value to list
            values.append(int(value))
        else:
            # skips over wrongly formatted data (temporary, fix to come soon)
            print("Inputted value is not numeric, skipping data")
else:
    # sets some input to value
    value = input("Enter a value: ")
    # checks if the end of the dataset has been reached
    while num_items != "end":
        # checks if value is a number
        if value.isnumeric():
            # adds value to list
            values.append(value)
        else:
            # skips over wrongly formatted data (temporary, fix to come soon)
            print("Inputted value is not numeric, skipping data")
        # sets some input to value
        num_items = input("Enter a value: ")
# if there are no numbers in values, ends program
if not values:
    print("No values entered. Ending program.")
    exit()
# loading message
print("Processing data...")
# sorts the dataset
values.sort()
# more code to go here
