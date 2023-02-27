def str_query(d, q):
    position_dict = dict() # Create empty dictionary

    for i in range(len(d)): # Iterate i through the first list d
        if d[i] in position_dict: # d[i] represents the word at that specific position
            position_dict[d[i]] = [i] # If the word is already in the dictionary, replace it with the most recent/highest i
        else: # If the word is not in the dictionary, use that index to denote where the word is
            position_dict[d[i]] = [i]

    for j in q: # Iterate through the second list q
        if j in position_dict: # If the word is a key (j) within the dictionary
            print(j, position_dict[j]) # Print the word and the position from the dictionary
        else: # If the word is not in the dictionary
            print(j, [-1]) # Return -1

    return position_dict

def includes(d, q):

    query_dict = {} # Create empty dictionary
    for i in range(len(d)): # Iterate through i, range is 0 to len(d) because (QUESTION!)
        if d[i] not in query_dict: # If the word at position i is not in the dictionay...
            query_dict[d[i]] = i # Add that key and value (position) to the dictionary

    for j in q: # Iterate through the second list q
        if j in query_dict: # If the word is a key within the dictionary
            print(j, "=", query_dict[j]) # Return the positions (values) of those words
        else:
            print(j, "=", -1)

def str_query2(d, q):
    dictionary = dict()
    i = 0
    for word in d: # Like TP 8.4 with the dictionary and index
        if word in dictionary:
            word_indice = dictionary[word]
            word_indice.append(i)
        else:
            dictionary[word] = [i]
        i+=1

        #if word not in position_dict:
        #    position_dict[word] = [i]
        #else:
        #    indices = position_dict[word]
        #    indices.append(i)
        #i+=1

    for j in q:
        if j in dictionary:
            print(j, dictionary[j]) # Returns the word in q and the value of the dictionary[key]
        else:
            print(j, -1)

d = ["the", "evening", "and", "the", "morning", "the", "sky", "is", "blue", "and", "pink"]
q = ["morning", "the", "green", "sky"]
#print(str_query(d, q))
print(str_query2(d, q))
#print(includes(d, q))