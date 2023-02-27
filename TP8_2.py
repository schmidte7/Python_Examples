def suffix(words):
    suff_dictionary = dict() # Create an empty dictionary
    suff_lower = [] # Create empty list for lowercased words

    for word in words: # Iterate throug the original word list
        suff_lower.append(word.lower()) # Append all lowercased words to the new list

    for word in suff_lower: # Iterate through new list
        if len(word) >= 2: # All words have to be 2 letters or more to have a suffix
            suffix = word[-2:] # Suffix is the two letters at the end of the word (key)

            if suffix in suff_dictionary: # If statement to check if the key exists in the dictionary
                suff_dictionary[suffix] = suff_dictionary[suffix] + 1 # Key already exists, add 1
            else: # If the key 'not in' the dictionary
                suff_dictionary[suffix] = 1 # Add the key and a value of 1

    most_words = [] # Create a new list for the most frequent words
    for key, value in suff_dictionary.items(): # Iterate through all of the keys and values of dictionary
         if value > 2: # Check only values that are 3 or more
            most_words.append(key) # Append the word to the new list to return the most frequent words
            #print(most_words,sep="\n")

    return most_words, suff_dictionary

def main():
    words = ["Voltaire", "the", "geat", "writer", "and", "poet", "was", "born", "in", "1694", "AS",
                   "François-Marie", "Arouet", "there", "and", "and"]
    print("\nstrings = ", words)
    print("---> suffix(strings) = ", suffix(words))

if __name__ == "__main__":
    main()
