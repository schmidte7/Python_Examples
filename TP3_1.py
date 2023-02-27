def char_position(string, character):

    i = 0 # For a while loop, start at position zero (0)

    while i < len(string)-1 and string[i] != character: # Iterate as long as you are in the string and the character is != to letter of the string
        i+=1 # Continue to add one until one of those statements is not True
    if string[i] == character: # If the string position and character are equal, return the position of the string
        return i # Return the position where c is located
    else:
        return False # Return False if character not in sting

def char_position2(string, character):

    for i in range(len(string)):
        if string[i] == character:
            return
    return False

def main():
    string = "sillybag"
    character = "b"
    print(char_position(string, character))
    print(char_position2(string, character))

if __name__=="__main__":
    main()