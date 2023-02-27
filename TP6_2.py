import numpy
T = numpy.array([1,17.5,-3,16,7]) # Array
S = {37,17.5,4,13,41,16,9} # Set

# Find the intersection or commonalities between the array and set
result = set() # Create empty set (no order and does not include duplicates)
for e in range(len(T)): # Iterate through an array
    v = T[e] # Set each position to another value (same as 5.2)
    if v in S: # If that value is also in S
        result.add(v) # Add that value into the result
print("1.", result)

A = {-7,5,8,9,13} # Set
B = {-7,2,5,6,8,9,13} # Set

# Find the union between A and B
result = set() # Create empty set (no order and does not include duplicates)
for itemA in A:
    result.add(itemA)
for itemB in B:
    result.add(itemB)
print("2.", result)

C = {-6.7,5,7.1,21.3,30} # Set
D = {-7.3, 1.17,3.45,6,7.1,9.3,21.3} # Set

# Delete common elements between two sets
for itemD in D:
    if itemD in C:
        C.remove(itemD)

print("3.", C)
