def appears_many(word_list):

    word_dictionary = dict() # Create an empty dictionary
    word_list_lower = [] # Create an empty list for the lowercased words

    for word in word_list: # Iterate through the original word list
        word_list_lower.append(word.lower()) # Lowercase all the words for equal comparison, append to new list

    for word in word_list_lower: # Iterate through the lowercased words
        if word not in word_dictionary: # If the words/values are not in the dictionary
            word_dictionary[word] = 1 # Add the word and a value of 1
        else: # If the word/value already exists...
            word_dictionary[word] = word_dictionary[word] + 1 # Add one to the value

    appears_once = set() # Create an empty set (no order or duplicates)
    for key, value in word_dictionary.items():  # Iterate through the dictionary
        if value == 1: # Set a threshold with the value
            appears_once.add(key) # Add those respective keys into the set

    appears_twice = [] # Create an empty list
    for key, value in word_dictionary.items(): # Iterate through the dictionary
        if value == 2: # Set a threshold with the value
            appears_twice.append(key) # Append the key associated with the value into the list

    appears_most_often = [] # Create an empty list
    for key, value in word_dictionary.items(): # Iterate through the dictionary
        if value >= 3: # Set a threshold with the value
            appears_most_often.append(key) # Append the key associated with the value into the list

    return word_dictionary, appears_once, appears_twice, appears_most_often

def main():
    word_list = ["a", "linear", "function", "is", "a", "function",
           "Each", "linear", "function", "has", "a", "straight", "line",
           "graph", "The", "addition", "of", "a", "linear", "of", "a",
           "linear", "function", "and", "another", "linear", "function",
           "is", "linear", "In", "linear", "algebra", "a", "linear",
           "function", "is", "a", "linear", "map", "a"]
    print(appears_many(word_list))

if __name__=="__main__":
    main()