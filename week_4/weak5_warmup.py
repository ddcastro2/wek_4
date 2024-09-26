# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
string1 = "abracadabra"
print(string1[4])
print(string1[-2])
firstC = (string1.find('c'))
print(firstC)
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[7:10])
print(alphabet[0:14:2])
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
presQuote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy "
presName = (presQuote[83:-1])
print(presName)
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
pyFun = "Python is fun. Fun is good. Good is subjective. "
print(pyFun.replace("Python is fun. Fun is good. Good is ", ""))
print(pyFun[0:-1:3])
print(pyFun[::-1])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
shout = "MAY THE FORCE BE WITH YOU"
calmDown = (shout.lower())
print(calmDown)
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
listMotto = ["Make", "haste", "slowly."]
stringMotto = " ".join(listMotto)
print(stringMotto)
splitStringMotto = (stringMotto.split("a"))
newStringMotto = " ".join(splitStringMotto)
print(newStringMotto)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
quote = "Life is what happens when you are busy making other plans."
print(quote.replace("busy", "distracted").replace("plans", "mistakes"))
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repeating = "iteration "
repeatingAndRepeating = repeating*7
print(repeatingAndRepeating)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
text = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
moonlight = "moonlight"
check = moonlight in text
print(check)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
loooong = "Supercalifragilisticexpialidocious"
howMuch = len(loooong)
print(howMuch)