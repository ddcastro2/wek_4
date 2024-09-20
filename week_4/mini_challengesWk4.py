# String Methods Practice #1
#slieds 12 -16
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper())
sentence2 = "ESPN IS THE BEST SPORTS NETWORK"
print(sentence2.lower())
print(sentence.replace("communications", "COMMUNICATIONS"))
print(sentence.replace("equivalent", "equal"))
# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
# word_list = ["Simple","is","better","than","complex."]
word_list = ["Simples", "is", "better", "than", "complex"]
print(word_list)
joined_sentence = "😍".join(word_list)
print(joined_sentence)
new_word_list = ["apple", "banana", "mango", "cherry", "watermelon"]
joined_sentence2 = "😂".join(new_word_list)
print(joined_sentence2)
sentence4 = "I am a python programmer"
print(sentence4.split())
print(sentence4.split(","))
print(sentence4.split("p"))
first_paragraph = "When, in the course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume, among the powers of the earth, the separate and equal station to which the laws of nature and of nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
new_para = (first_paragraph.replace("people", "citizens")).replace(",", "😊").replace(" ", "")
print(new_para)

# String Methods Practice #3
# Replace in the following sentence:
# "If the implementation is hard to explain, it might be a bad idea."
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.
new_sentence = "if the implementation is hard to explain, it might be a bad idea"
mod_sent = (new_sentence.replace("hard", "easy")).replace("bad", "good")
print(mod_sent)
#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.
result = "Repitiion " * 15
print(result)
# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998
haiku = "Whitecaps on the bay: A broken signboard banging, In the April wind."
beach = "beach"
results = beach in haiku
print(results)

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
amounts = len("electroencephalographist")
print(amounts)