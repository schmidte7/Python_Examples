def most_frequent_prefix(strings):

    prefix_dictionary = dict() # Create empty dictionary
    prefix_list = [] # Empty list for lowercased words

    #frequent_prefix = None # frequent_prefix will contain the result of the function (the most frequent prefix)
    # max_count = 0 # max_count will contain the count of frequent_prefix (the most frequent prefix)
                    # both (frequent_prefix and max_count) will be updated at the same time (when needed.. see below)

    for words in strings: # Iterate through the first list
        prefix_list.append(words.lower()) # Lowercase everything and append to new list

    for word in prefix_list: # Iterate through the lowercased list
        if len(word) >= 2: # If the word's length is 2 or more...
            prefix = word[:2] # Grab the prefix of each word

            if prefix in prefix_dictionary: # If the key/value already exists...
                prefix_dictionary[prefix] = prefix_dictionary[prefix] + 1 # Add one to the value
            else: # If the key/value does not exist
                prefix_dictionary[prefix] = 1 # Create the key/value, with a value of 1

           # count = prefix_to_count[prefix] # Retrieve the count of prefix
           #  if count > max_count: # If the count of prefix is not the maximum count then we update both max_count and frequent_prefix
             #   max_count = count # Set the new count
             #   frequent_prefix = prefix # Set the new most frequent prefix

    most_frequent_1 = [] # Create a list for most frequent words
    most_frequent_2 = [] # Create a list for most frequent words
    for key, value in prefix_dictionary.items(): # Iterate through the dictionary
        if value >= 2: # Set value to a certain limit
            most_frequent_1.append(key) # Append the keys where that value is true

    for key, value in prefix_dictionary.items(): # Iterate through the dictionary
        if value > 2:  # Set value to a certain limit
            most_frequent_2.append(key) # Append the keys where that value is true

    return most_frequent_1, most_frequent_2  #frequent_prefix

def prefix_to_indices(strings):

    prefix_dictionary = dict() # Create empty dictionary
    prefix_list = [] # Empty list for lowercased words

    for words in strings: # Iterate through the first list
        prefix_list.append(words.lower()) # Lowercase everything and append to new list

    i = 0
    for word in prefix_list: # Iterate through the lowercased list
        if len(word) >= 2: # If the word's length is 2 or more...
            prefix = word[:2] # Grab the prefix of each word

            if prefix in prefix_dictionary: # If the key is in the ditionary
                word_indice = prefix_dictionary[prefix] # Add a value to the dictionary key
                word_indice.append(i) # This line adds the i (indice) if the key,value already exists
            else:
                prefix_dictionary[prefix] = [i] #  If the key, value does not exist, the value is set to a list []
        i+=1 # To iterate through the strings, need to increment by 1 for the next indice/position of the prefix (key)

    return prefix_dictionary

def main():

    strings=["TODAY", "the", "sun", "is", "shining", "and", "the", "sky", "is", "blue", "blue", "blue"]
    print("\ntext = ", strings)
    print("---> most_frequent_prefix(text) = ", most_frequent_prefix(strings))
    print("---> prefix_to_indices(text)    = ", prefix_to_indices(strings))

if __name__=="__main__":
    main()