def starts_with(s,a,query):
    if a < 0 or a >= len(s):
        raise Exception("")
    else:
        i = a # Start iterating i at position a or 4
        j = 0 # Iterate through the query
        while j < len(query): # While j is less than the length of the query
            if query[j] != s[i]: # If the two letters do not equal
                return False # Immediately return False
            else: # If the string letter and query letters match at first...
                j+=1 # Iterate query to check next letter
                i+=1 # Iterate string to check next letter
        return True

def indices_of_query(s, query):
    indices = [] # Create empty list

    for i in range(len(s)): # Iterate through the string
        if starts_with(s=s,a=i,query=query): # Need to set equal the certain elements. a comes from the
                                             # first function, i the current. Need to assign i to a
            indices.append(i) # Add the position of where the query appears
    return indices

def main():
    s = "capitol capitol"
    a = 3
    query = "it"
    print(starts_with(s,a,query))
    print(indices_of_query(s,query))

if __name__=="__main__":
    main()


