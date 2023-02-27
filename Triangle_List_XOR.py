def p2(k: int) -> list[int] :

    row = [1] # Create list with first position (0) as 1 (this will be overwritten each time the second loop runs by nextrow)
    for i in range(2, k+1): # If k = 5 (which is set), for range 2:k includes 2, 3, 4. Need to do k+1 to start at 2 and include 5. i = 2
        nextrow = [1] # Position 0, will add other numbers in the second for loop
        for j in range(1, i-1): # ("get to" i = k) Always start at position 1 and go to i-1. For example, if i=5, there will be three
                                # positions that need to be looped (1, 2, 3), 0 already = 1 and 4 will = 1 in a later step
            nextrow.append((row[j-1]+row[j]) % 2) # For position j-1 and j in row (look prior). Add them togeher, if they
                                                  # are divisable by 2, then append 0 else 1 to the nextrow
        nextrow.append(1) # Append 1 to the end of the list
        row = nextrow # Set nextrow = row so that it 'saves' row for the i iterator to create the following row
    return nextrow # or row

def p(k: int) -> list[int]:

    row = [1] # Create list with position 0 as 1
    for i in range(k-1): # Iterate through k (given)
        row = [row[j] ^ row[j + 1] for j in range(len(row) - 1)]
        row = [1] + row + [1]
    return row

print('Question 1')
print('test')
print(f'k=3: {p2(2)}')
print(f'k=3: {p2(3)}')
print(f'k=3: {p2(4)}')
print(f'k=5: {p2(5)}')
print(f'k=5: {p(5)}')