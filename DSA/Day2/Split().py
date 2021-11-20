#w3schools.com/python/ref_string_split.asp

txt = "welcome to the jungle"

x = txt.split()

print(x)

#1.Split the string, using comma, followed by a space, as a separator:
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)

#2.Use a hash character as a separator:

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

#3.Split the string into a list with max 2 items:

txt = "apple#banana#cherry#orange"

#setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)