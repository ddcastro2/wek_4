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


######sets#########
# sets are unordered and unindexed
# they are defined using curly brackets {these}
# they do not allow duplicates
fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
print(fruits)
# print(dir(fruits))
# # # print(help(fruits))
# # print(len(fruits)) # number of elemnts in the set
# # print("volvo" in fruits) #asks if a certain value is in the set
# print(fruits.add("orange"))
# print(fruits)
# print(fruits.add("kiwi"))
# print(fruits)
print(fruits.update(["orange", "kiwi", "pineapple"]))
print(fruits.remove("banana"))
print(fruits.pop) # remove the last element
print(fruits.clear())
print(fruits)

social_security_number = {123456789, 987654321, 123456789}
print(social_security_number)
print(social_security_number.pop)
print(social_security_number)
print(social_security_number.add(135792468))
print(social_security_number)

example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(example_tuple)
print(example_tuple.count(2)) #number of times the number 2 appears
print(dir(example_tuple)) #attributes that can be used with tuples
print(len(example_tuple))
print(2 in example_tuple)
print(example_tuple.index(2))
# lymeric = "peter piper picked a peck of pickled peppers"
# #CONVERT INTON A TUPLE
# #split it first
# lymerica_tuple = tuple(lymeric.split())
# print(lymerica_tuple)
# print(lymerica_tuple.count("p"))

# for item in example_tuple:
#     print(item)


#############dictionaries#############
# a collection of {key:value} pairs, no duplicates
capitals = {"America":"Washington D.C",
            "China":"Beijing",
            "Rwanda":"Kigali",
            "Tanzania":"Odoma",
            "Uganda":"Kampala",
            "Kenya":"Nairobi"}
print(capitals)
print(dir(capitals))
# print(help(capitals))
print(len(capitals))
print(capitals["Kenya"])
print(capitals.get("Kenya"))
capitals["South Africa"] = "Pretoria"
print(capitals)
capitals.update({"Nigeria":"Abuja"})
print(capitals)
capitals.update({"France":"Paris"})
capitals.update({"Russia":"Moscow"})
capitals.update({"Algeria":"Algiers"})
print(capitals)
capitals.pop("China")
print(capitals)

for key in capitals:
    print(f"These are the {key}" + "ns")


for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in items:
    [print(f"{value} is the capital of {key}")]