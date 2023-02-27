def remove_duplicates(x):

    duplicates = []

    # Similar to TP 5.2
    # If you only use i and not e, it will return the actual positions and not the position of the element
    for i in range(len(x)): # Iterate through the list
        e = x[i] # Set a new value to each position in the list
        if e not in duplicates: # If that element in not in the list
            duplicates.append(e) # Add e to the duplicates list
    return duplicates

def remove_dups(x):

    remove_list = [] # Create empty list

    for i in x: # Iterate through the list of x
        if i not in remove_list: # If the i is not already in the created list
            remove_list.append(i) # Add the i to the remove_list
    return remove_list

def remove_dups2(x):
    remove_set = set()
    remove_list2 = []

    for i in x:
        remove_set.add(i)

    for i in remove_set:
        remove_list2.append(i)
    return remove_list2

def main():
    x = [2,3,4,5,4,2]
    print(remove_duplicates(x))
    print(remove_dups(x))
    print(remove_dups2(x))

if __name__=="__main__":
    main()