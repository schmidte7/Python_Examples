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

def main():
    s = "capitol capitol"
    a = 4
    query = "top"
    print(starts_with(s,a,query))

if __name__=="__main__":
    main()


    #if a < 0 or a >= len(s):
    #    raise Exception("")
    #else:
    #    i = a
    #    j = 0

    #    while j < len(query):
    #        if s[i] == query[j]:
    #            i += 1
    #            j += 1
    #        else:
    #            return False

    #        if j >= len(query):
    #            return True