"""
PART 1
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.
To ensure security, a valid passphrase must contain no duplicate words. How many are valid given the dataset provided?
For example:
aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
"""

#Import Data File
x = open("./DataInputs/Day4.txt","r").read().splitlines()
print("Data imported from: \"./DataInputs/Day4.txt\"")

#Defines the function to check for a valid password by comparing the set of unique words against the total number
def PasswordCheck(password):
    contents = password.split()
    if len(contents) == len(set(contents)):
        return True
    else:
        return False

#Loops through data checking for the number of unique passwords

CheckList = x
numValid = 0
numInvalid = 0
for item in CheckList:
    if PasswordCheck(item):
        numValid += 1
    else:
        numInvalid += 1
        
print("Valid passwords for a repeat word check: " + str(numValid))


"""
PART 2
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is,
a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.
For example:
abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
"""

"""
Defines and executes a sorted() function on the data set. Took a lot of reading about sorting lists by their characters. I then based this upon another contributors
response in the subreddit for the proper syntax

"""
anagramValid = 0
def anagramCheck(data):
    anagramValid = 0
    for line in data:
        x = ["".join(sorted(i)) for i in line.split()]
        if len(x) == len(set(x)):
            anagramValid += 1
    return anagramValid
       
print("Valid passwords for an anagram check: " + str(anagramCheck(x)))

