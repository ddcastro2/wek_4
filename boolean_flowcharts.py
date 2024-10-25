#Exercise 1
fav_lang = input("What is your favorite coding language? ")
if fav_lang == 'Python':
    print("Your favorite language is Python!")
else:
    print("Different Choice")
#Exercise 2
num = int(input("Choose a number to determine its place on the grading scale: "))  
if num >= 90:
    print("This grade is an A")
elif 80 <= num <= 89:
    print("This grade is a B")
elif 70 <= num <= 79:
    print("This grade is a C")
elif 60 <= num <= 69:
    print("This grade is a D")
elif num < 60:
    print("This grade is an F")
else:
    print("The number you inputted was invalid")
#Exercise 3
user = input("Username: ")
logged_in = False
if user == 'admin' and logged_in:
    print("Welcome admin!")
elif user == 'admin' and not logged_in:
    print("Please log in")
elif not user == 'admin' and logged_in:
    print("Sorry, that user does not have acces.")
else:
    ("Invalid Input")
#Exercise 4
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
if list_1 is list_2:
    print("These are the same object")
else:
    print("These are the NOT the same object")