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

def find_pal(s,k):
    if k < 1:
        raise Exception("The value of k needs to be greater than 1.")
    for i in range(len(s)-k): # Iterate through the range of string - k (how many letters in the palidrome)
        if isPalidrome(s,start=i,end=i+k-1): # If the positions of start and end contain a palidrome with the specified k value
            return i # Return the position where it first occurs
    return -1 # Return -1 if the palidrome does not exist

def main():
    s = "abcdeffedcquipopz"
    k = 3
    print(find_pal(s,k))

if __name__=="__main__":
    main()