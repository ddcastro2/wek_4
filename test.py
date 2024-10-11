newPhrase = "rainstorm"
            #012345678
            #123456789 -- college board version
#create a new variable called shortPhrase
# and assign it a value by slicing
#the newPhrase variable byy removing
# the first three characters
# and the last three characters
# the first three characters are "rai"
# the last three characters are "orm"
#substring(string, start, end)

shortPhrase = newPhrase[3:len(newPhrase)-3]

print(shortPhrase)
