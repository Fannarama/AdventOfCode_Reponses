"""
Part 1
The object of this puzzle is to escape a "maze" by moving through a list of numbers until you may make a move that pushes you outside the bounds of the list.
Examples given dictate the rules as follows:
- The number you are on for that current step defines where you move next
- If it is negative you move that many steps upward in the list (or left if the list is redefined as horizontal)
- If it is positive you descend that many steps, the example given is if a value of '2' is provided then you skip the next number and begin your next step
on the number after the one which you skipped
- Following each step you += that value by 1, this does not affect the steps you take for that turn but will affect the next time you land on that value.
For instance if you land on a 3 you will advance 3 spaces, but you will incriment that 3 to now be a 4. Thus, if later on in the puzzle you encounter that
space again you will now advance 4 spaces instead.

The goal is to establish how many steps it will take to escape the data set provided.
"""

#Import data and populate the list
x = open("./DataInputs/Day5.txt","r").read()
print("Data imported from: \"./DataInputs/Day5.txt\"")
data = [int(n) for n in x.split()]
data2 = [int(n) for n in x.split()]

#Iniatilize variables
location = 0
total = 0

#Iterate through the "maze"
while location <= (len(data)-1) and location >= 0:
    nextloc = location + data[location]
    data[location] += 1
    total += 1
    location = nextloc
else:
    print("Part1 Total Steps: " + str(total))

"""
Part 2
-Now if the offset was >= 3 decrease the value by 1 instead of increasing
"""
#Redefine the location and totals
location2 = 0
total2 = 0

#Iterate through with new rules
while location2 <= (len(data2)-1) and location2 >= 0:
    if data2[location2] >= 3:
        nextloc = location2 + data2[location2]
        data2[location2] -= 1
        total2 += 1
        location2 = nextloc
    else:
        nextloc = location2 + data2[location2]
        data2[location2] += 1
        total2 += 1
        location2 = nextloc
else:
    print("Part2 Total Steps: " + str(total2))