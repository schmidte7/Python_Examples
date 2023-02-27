def triangleSubGraph(g):

    triangleSub_list = [] # Create an empty list to store subgraphs

    for x, nodes_of_x in g.items(): # Iterate through the dictionary for key (a) and values (a,b,c)
        for y in nodes_of_x: # Choose another value inside of a values (b)
            if x !=y: # If a and b are not equal... (do not want to loop over itself)
                nodes_of_y = g[y] # Pull the values from the dictionary for the b key and its values (a, c)
                for z in nodes_of_y: # Loop through the last key (c)
                    if z in nodes_of_x and z !=x and z!=y: # If c is in the values of x and does not equal a and b...
                        triangleSub = {x,y,z} # Create a subgraph value with those three keys (can also use list but will be repetitive)
                        if triangleSub not in triangleSub_list: # Check to see if that triangleSub is already in the list
                            triangleSub_list.append(triangleSub) # If it is not, append to the over list for an output
    return triangleSub_list

def main():
    ''' Test case 1 '''
    g = {'a': {'b', 'c', 'a'}, 'b': {'a', 'c'}, 'c': {'a', 'b', 'd'}, 'd': {'c'}}
    # print("\ng1 = ", g1)
    print("---> triangleSubGraph(g=g1) = ", triangleSubGraph(g))

    ''' Test case 2 '''
    g2 = {'a': {'b', 'a'},
          'b': {'a', 'b', 'c'},
          'c': {'b', 'd', 'e'},
          'd': {'c'},
          'e': {'c'}}


    #print("\ng2 = ", g2)
    print("---> triangleSubGraph(g=g2) = ", triangleSubGraph(g=g2))

if __name__ == "__main__":
    main()