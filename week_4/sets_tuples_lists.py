# collection = single "variable" used to store multiple values
# list = [] ordered and changeable. Duplicates OK
# set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "pineapple", "kiwi", "watermelon", "starfruit", "grapes", "strawberries", "mango"]

print(fruits[::2])
print(fruits[::-1])
# ::2 gives every two items in the index
# 0: gives me the first one all the way to the end, not 0:3 because 3 is exclusive and using 4 will lead to an error
# ::-1 gives everything in your list backwards
for fruit in fruits:
    print(fruit)
# this iterates over your list 
# "FOR every FRUIT in FRUITS"
# Iteration is going through the entire list and is using the variable, "fruit", and making it so fruit = (whatever fruit it has landed on)
    # it goes through the list multiple times, for example, the first time being fruit = apple, then goes again, fruit = orange
print(dir(fruits))

#ABLE TO BE UNCOMMNTED:
# print(help(fruits)) - commenting this out for now to give space in the terminal

# Dir is listing all attributes of the list, sort of all the documentation, sort of a list of what you can do with your list
# help gives you the "manual" of your list
print(len(fruits))
#gives you the length of your list
print("pineapple" in fruits)
# This basically just checks to see if a certain value is in your list's index
# Think of it as it saying "Pineapple in fruits?", then it prints out True or False in response to that "question"

# ABLE TO BE UNCOMMENTED:
# fruits[0] = "pineapple"
# # this replaces or reassigns the 0 value with whatever you desire
# for fruit in fruits:
#     print(fruit)
# now it prints out the new interation with pineapple being shown twice because it now has it's own value as well as the new one it was assigned, replacing apple

fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapple")
# append: it adds something to the END of the list. So it adds another value to end of the list.
# remove: just removes a value
# insert: puts in a new value but does NOT replace it, sort of like it squeezes it in and pushing the other values giving other ones a different value such as mango being 12 instead of 11
fruits.sort()
fruits.reverse()
# using sort + reverse prints it out in reverse alphabetical order

# fruits.clear()
# clears out everything, list is empty and will only print []

print(fruits)
print(fruits.index("apple"))
