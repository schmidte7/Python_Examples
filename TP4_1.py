def isPalidrome(s, start, end):

    if start < 0 or end >= len(s) or start > end:
        raise Exception("One of the inputs is incorrect!")
    else:
        a = start # Starting position begins at specified value in main(), start assigns a value to a (3)
        b = end # Ending position begins at specified value in main(), end assigns a value to b (6)

        while a < b: # a must be smaller than b since reading left to right
            if s[a] != s[b]: # If those positions are not the same letter
                return False # Return False
            else: # If those two letters are the same
                a+= 1 # Increase a by one
                b-= 1 # Decrease b by one
        return True # Return True if all letters match

def main():
    s = "heolloway"
    start = 2
    end = 5
    print(isPalidrome(s, start, end))

if __name__=="__main__":
    main()