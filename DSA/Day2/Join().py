#Join all items in a tuple into a string, using a hash character as separator:

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

# Syntax
# string.join(iterable)
# Parameter Values
# Parameter	Description
# iterable	Required. Any iterable object where all the returned values are strings
# More Examples
# Example
#Join all items in a dictionary into a string, using a the word "TEST" as separator:

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)