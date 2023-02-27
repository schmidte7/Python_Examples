def is_dangling_triangle_free(g: dict[str, set[str]]) -> bool :

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
                            if len(g[x])+len(g[y])+len(g[z]) == 7: #Remark: if {a,b,c} is a dangling triangle, no. neigbours of a + no. neighbours of b + no. neighbours of c is exactly 7.
                                return False
    return True

def is_dangling_triangle_free2(g: dict[str, set[str]]) -> bool :
    for n1 in g: # Iterates over all nodes in the graph
        for n2 in g[n1].difference(set([n1])): # For each node, iterates over neighors and used to get the set of neighbors that are not in the current node (n1 compared to n2)
            for n3 in g[n2].difference(set([n1,n2])): # For each node, iterates over neighors and used to get the set of neighbors that are not in the current node (n1 and n2 compared to n3)
                if n1 in g[n3]: # If node 1 is in n3's values
                    # n1,n2,n3 is a triangle
                    if len(g[n1])+len(g[n2])+len(g[n3]) == 7: # The length of the nodes values = 7 (b,c) + (a,c) + (a,b,d)
                        # this is a dangling triangle
                        return False # If the triangle has a dangle...
    return True # If the triangle does not have a dangle...

# Exactly one neighbor, not related to dangling triangles
def is_dangling_triangle_free3(g: dict[str, set[str]]) -> bool :
    # Iterate over all nodes in the graph
    for node in g:
        # Check if the node has exactly one neighbor
        if len(g[node]) == 1:
            # Get the neighbor
            neighbor = next(iter(g[node]))
            # Check if the neighbor also has exactly one neighbor
            if len(g[neighbor]) == 1:
                # If both nodes have exactly one neighbor, then they form a dangling triangle
                return False
    # If no dangling triangles were found, return True
    return True

g = {'a': {'b','c'}, 'b':{'a','c'},'c': {'a','b','d','h'}, 'd':{'c','e','i'},'e': {'d','f','g'},
     'f': {'e','g'}, 'g': {'e','f'}, 'h': {'c','i','k'}, 'i': {'d','h','k'}, 'j': {'l','m'},
     'k': {'h','i','m'}, 'l': {'j','m'}, 'm': {'l','k','j'} }

print('Question 4')
print(f'test with g={g}')
print(is_dangling_triangle_free(g))
print(is_dangling_triangle_free2(g))
print(is_dangling_triangle_free3(g))
print()