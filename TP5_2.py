A = [] # Create an empty list
B = [1,2,3,4,5,6,7,8,9,10,11,12]
C = [3,5,3,6,7,1,8,2]

first_index = 0 # Index for even values in the list
last_index = 0 # Index for odd values in the list

for e in B: # Iterate through the list B
    if e % 2 == 0: # If a number can be divided by 2 with a remainder 0 --> even numebr
        A.insert(first_index, e) # Insert the even number always at position 0
    else: # If the number has a remainder --> odd number
        A.insert(last_index,e) # Insert the odd number at 0, then continue to add to the right
    last_index+=1 # Through each loop, add one to the last_index for odd numbers

print("4.", A)

for e in range(3): # Only look at three values within the range
    B.pop(-1) # Start at the end of the list
    # B.pop(len(B)-1) # Another way to remove the last three values

print("5.", B)

for e in range(3): # Only look at three values within the range
    B.pop(0) # Start at the beginning of the list

print("6.", B)

for e in B: # Iterate through B first because you will remove from C
    if e in C: # If the element in B is also in C
        C.remove(e) # Remove the element in C that also appeared in B

print("7.",C)

import numpy # File -> Settings -> Project: "" -> Python Interpreter

T = numpy.array = ([1,2,3,4,5]) # Create an array
D = [] # Create another empty list
P = [] # Create empty list to test

for i in range(len(T)-1,-1,-1): # Iterate through an array backwards starting at last position
    e = T[i] # Set the position of T to e to append to another list
    D.append(e) # Append e to list D

print("10.", D)

# Iterate backwards through a list
wordList = ["I","like","eggs"]
for i in range( len(wordList)-1, -1, -1):
    e = wordList[i]  # Set the position of T to e to append to another list
    P.append(e)  # Append e to list P

print("Extra:", P)
print("Second position backwards:",P[-2]) # Pulls the second to last value from the end
