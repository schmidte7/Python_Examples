A = {"John":33,"Michael":51,"Del":25,"Chuck":44}
B = {"Chuck":44,"Dan":73,"Sean":54,"Michael":51,"Amy":42}

# Find the intersection or commonalities between the dictionaries
intersection_dict = dict() # Create an empty dictionary
for keyA, valueA in A.items(): # Iterate through A's keys and values
    if keyA in B: # If keyA is in B...
        valueB = B[keyA] # Set B's values
        if valueA == valueB: # If the two values are equal (since we already checked the keys)
            intersection_dict[keyA] = valueA # Add the key and dictionary of A or B into the new dict
print(intersection_dict)

# Delete common elements between two dictionaries
for keyB, valueB in B.items(): # Iterate through B's keys and values since deleting from A
    if keyB in A: # If keyB is in A...
        valueA = A[keyB] # Set A's values
        if valueB == valueA: # If the two values are equal (since we already checked the keys)
            del A[keyB]  # Since the keys are the same, use keyB and delete from dictionary A
print(A)