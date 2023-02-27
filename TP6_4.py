def commmonStrings(A, B, C):
    result = set() # Create an empty set

    A_lower = set() # Create empty set for list A
    for e in A: # Iterate through the list
        A_lower.add(e.lower()) # Add the lowercased words into the set (does not contain duplicates)

    B_lower = set() # Create empty set for list B
    for e in B: # Iterate through the list
        B_lower.add(e.lower()) # Add the lowercased words into the set (does not contain duplicates)

    C_lower = set() # Create empty set for list C
    for e in C: # Iterate through the list
        C_lower.add(e.lower()) # Add the lowercased words into the set (does not contain duplicates)

    # Similiar to 5.2 with lists but these are sets
    # Check what is in A/B or A/C
    for itemA in A_lower: # Iterate through the new set of words in A_lower
        if (itemA in B_lower) or (itemA in C_lower): # Compare A_lower to B_lower and A_lower to C_lower (do not need () )
            result.add(itemA) # Add result of itemA to result (set)

    for itemB in B_lower: # Iterate through the new set of words in B_lower
        if itemB in C_lower: # Compare B_lower to C_lower
            result.add(itemB) # Add result of itemB to result (set)

    return result

def main():
    A = ["I", "went", "to", "her", "office"]
    B = ["My", "cousin", "Mary", "arrived", "at", "her", "apartment"]
    C = ["Joseph", "Arrived", "at", "9am", "to", "his", "office"]
    print(commmonStrings(A, B, C))
if __name__=="__main__":
    main()