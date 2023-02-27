def substring(s, sub):

    if len(sub) > len(s): # If the length of the substring exceeds the string
        return False # Return False
    else: # If the substring is less than the string
        i = 0 # Iterator through string
        while i < len(s) : # Iterate through the length of the string
            exitLoop = False # Assign value as False/0
            j = 0 # Iterator through substring
            while j < len(sub) and not exitLoop : # Iterate through the substring, J VARIES BETWEEN 0 AND LEN(SUB)-1 and exitLoop not = 1 (True)
                if s[i+j] == sub[j]: # Now check again that the positions align and switch 0 to j in sub
                    j+=1 # Keep i constant in first loop, but add j to move both string and substring
                else: # If they do no match, exit the loop
                    exitLoop = True # Take that value away (1/True) - breaking the loop

            if j >= len(sub) : # Once j is = or greater than the sub length (means it has reached the end)
                return i # Return the position
            else:
                i+=1 # If not at the end, go through the i loop again to look at the next set of i and j

        return False

def main():
    s = "hellollup"
    sub = "lu"
    print(substring(s,sub))

if __name__=="__main__":
    main()