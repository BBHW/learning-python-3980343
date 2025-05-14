# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values

mylist = [0.5, 1, "two", True, 9,8,7]
# print(len(mylist))



# to access a member of a sequence type, use []

# add a list to another list

anotherList = [1, 3, 3]
mylist2  = mylist + anotherList
print(mylist2)
# use slices to get parts of a sequence

print(mylist[0:2:2])

# you can use slices to reverse a sequence


# Tuples are like lists, but they are immutable


# Sets are also sequences, but they contain unique values

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
