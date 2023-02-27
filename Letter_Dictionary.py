def indexing(t: str, ks: list[str]) -> dict[str, list[int]] :
    result = {}  # Create an empty dictionary
    t_lower = text.lower() # Lowercase all the words for comparison
    for k in ks: result[k] = set()  # Iterate through the list, and put values of dictionary to set
    for a in range(len(t_lower)):  # Iterate through the length of the text
        for k in ks:  # Iterate through the list words again
            if a + len(k) < len(t_lower) and k == t_lower[a:a + len(k)]:
                # Make sure that the length of k + index a is less than overall t  # Position of text[1 to 1+length of k (4) -> 1:5)
                result[k].add(a)  # Add the index to the value (set) in the dictionary
    return result

def indexing2(t: str, ks: list[str]) -> dict[str, list[int]] :
    index = {}  # Create an empty dictionary
    text_lower = text.lower() # Lowercase the entire string

    for k in ks:
        if k not in index:
            index[k] = set([])

        for a in range(len(t)):  # Iterate through the length of the text
            if k == text_lower[a:a + len(k)]:
                # Make sure that the length of k + index a is less than overall t  # Position of text[1 to 1+length of k (4) -> 1:5)
                index[k].add(a)  # Add the index to the value (set) in the dictionary
    return index

print('Question 2')
text = 'Assignment: draw the scatterplot for the CAT category'
kwds = ["cat", "sign", "on", "or", "ass", "my"]
print(f'test with text="{text}" and keywords={kwds}')
#print(indexing(text, kwds))
print(indexing2(text,kwds))
print()