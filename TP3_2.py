def pal(s):
    res = True
    i = 0 # Start at the beginning of the word
    j = len(s)-1 # Start at the end of the word
    while i < j and res == True : # Iterate through word while i is less than j (they will pass each other)
        if s[i] == s[j]: # If the two letters match...
            i+= 1  # Add one to the beginning iterator
            j-= 1  # Subtact one from the ending iterator
        else: # If the letters are not equal, get out of loop
            res = False
    return res

s="coloc"
res=pal(s)
if res: # If res = True
    print("this string is palindrome")
else: # If res = False
    print("this string isnt palindrome")

def palidrome(S):

    i = 0 # Start iterating from the left at position zero (0)
    j = len(S)-1 # Start iterating from the right at the end of the word

    while i < j: # Alt.  'while i < len(word)-1', iterate through until i >= j
        if S[i] == S[j]: # If the two letters are equal...
            i+=1 # Increase i by one
            j-=1 # Decrease j by one
        else:
            return False # Return false if one of the letter combos do not match
    return True # Return True when i = j because you have gone through the entire string and everything aligns
def main():
    S = 'COLOC'
    print(palidrome(S))

if __name__ == "__main__":
    main()

def isPalindrome(s):
    return s == s[::-1] # Return the slice of the string that starts at the end and steps backward one element at a time

def main():
    s = "kayak"
    ans = isPalindrome(s)

    if ans: # If the word forward and backwards matches
        print("Yes")
    else: # If the words forward and backwards do not match
        print("No")

if __name__=="__main__":
    main()

