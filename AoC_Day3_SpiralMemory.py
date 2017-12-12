#Part 1
"""Data is presented in a spiral pattern outward from 1 at the center,
you are tasked with finding the number of steps required to get to a given data point
via its Manhattan distance between itself and the origin of '1'."""
from math import sqrt

dataVal = input("Please provide a number: ")
dataVal = int(dataVal)
lowersquare = int(sqrt(dataVal))

if lowersquare % 2 == 0:
    uppersquare = lowersquare + 1
    lowersquare = lowersquare - 1
else:
    uppersquare = lowersquare + 2
ring = int((uppersquare/2)-.5)

corner0 = uppersquare**2 - 4*(uppersquare-1)
corner1 = uppersquare**2 - 3*(uppersquare-1)
corner2 = uppersquare**2 - 2*(uppersquare-1)
corner3 = uppersquare**2 - 1*(uppersquare-1)

if dataVal > corner0 and dataVal <= corner1:
    midpoint = corner1 - ring
    stepy = abs(midpoint - dataVal)
if dataVal > corner1 and dataVal <= corner2:
    midpoint = corner2 - ring
    stepy = abs(midpoint - dataVal)
if dataVal > corner2 and dataVal <= corner3:
    midpoint = corner3 - ring
    stepy = abs(midpoint - dataVal)
if dataVal > corner3 and dataVal <= uppersquare**2:
    midpoint = (uppersquare**2) - ring
    stepy = abs(midpoint - dataVal)

print("deltaX: ",ring)
print("deltaY: ",stepy)
print("Total Steps: ",ring+stepy)

#Part 2
#This takes the squares and makes them the sum of their adjacent already filled in squares, the goal is to find a number larger than the initial input
#A lot of this one was borrowed from the subreddit, as I was not really familiar with how to set up dictionaries like this. Very informative though.
def next_coord(x,y):
    if x == y == 0: return (1,0)
    if y > -x and x > y: return (x, y+1)
    if y > -x and y >= x: return (x-1, y)
    if y <= -x and x < y: return (x, y-1)
    if y <= -x and x >= y: return (x+1, y)
    
x, y = 0, 0
vals = { (0, 0): 1}
while vals[(x, y)] <= dataVal:
    x, y = next_coord(x, y)
    vals[(x, y)] = sum(vals.get((x+i, y+j), 0) for i in [-1, 0, 1] for j in [0, 1, -1])
print(vals[(x,y)])