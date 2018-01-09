"""
This solution was heavily borrowed from a subreddit response, as I had to learn what a tuple was for this day of AoC and I had yet to really see one.
"""

def distribute(banks):
    # This is the number of values we need to redistribute.
    m = max(banks)
    index = 0
    # First value matching the maximum
    for i, val in enumerate(banks):
        if val == m:
            index = i
            break
    # Zero out the value we start at.
    banks[index] = 0
    # Redistribute
    while m != 0:
       index += 1
       index %= len(banks)
       banks[index] += 1
       m -= 1

def solve(banks, count_second):
    # Keep a set of seen states.
    seen = set()
    count = 0

    # Iterate until we get a repeat state.
    while tuple(banks) not in seen:
        # Add a tuple to our seen states since lists aren't hashable (learned
        # this the hard way).
        seen.add(tuple(banks))
        # Redistribute the banks -- note that lists are passed by reference so
        # this will mutate banks.
        distribute(banks)
        count += 1
    # If we're going to count the secondary iterations, then recurse.
    if count_second:
        # Get the count starting anew from the last state.
        return solve(banks, False)
    # Otherwise, return the desired count.
    else:
        return count

with open('./DataInputs/Day6.txt') as inp:
    # Parse the input. 
    banks = list(map(int,inp.read().strip().split())) 
    # Part 1.
    print(solve(banks, False))
    # Part 2.
    print(solve(banks, True))