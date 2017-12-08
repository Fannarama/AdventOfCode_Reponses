""" Part 1 takes a sequence of digits and finds the sums of all digits
that match the next digit in the list. This is circular and has the last digit
interacting with the first.
"""

#Check to see if input is an integer sequence
n = 0
while True:
  try:
     n = int(input("Please provide a whole number sequence: "))       
  except ValueError:
     print("Please try again")
     continue
  else:
     break

#Establish variables
total = 0
s = str(n)

#Loop through sequence checking if adjancent number is equal and then adding to 'total'
for x in range(len(s)):
    if x < len(s)-1:
        if s[x] == s[x+1]:
            total += int(s[x])
    elif x == (len(s)-1):
        if s[x] == s[0]:
            total += int(s[x])
    else:
        break
    
print("Part 1: "+ str(total))

#PART 2
"""
Part two dictates that the digit must match the accompanying digit that is halfway around the circular loop, or 'half of the length' steps forward
"""
#Establish variables
total2 = 0
halfLen = int(len(s)/2)

#Loop through sequence checking if the number 1/2 the total length of the sequence away is equal and then adding to 'total2'
for x in range(len(s)):
    if x < halfLen:
        if s[x] == s[x+halfLen]:
            total2 += int(s[x])
    elif x >= halfLen:
        if s[x] == s[x-halfLen]:
            total2 += int(s[x])
    else:
        break
    
print("Part 2: "+ str(total2))
