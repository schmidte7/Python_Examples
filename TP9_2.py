def check_k_clique(subGraph, k, g) :

    if k != len(subGraph): # If k and the length of subgraph do not equal,
        return False # Return False (did not find the clique)
    else: # If the length of subgraph and k are equal... continue
        for a in subGraph: # Iterate through each node in the subgraph (a, b, c)
            nodes_of_a = g[a] # Start with a and grab its values from the dictionary (b, c)

            for b in subGraph: # Iterate through the second node of the subgraph
                if a != b and b not in nodes_of_a: # If a is not equal to b and b in not included in a's values...
                    return False # Return False

        return True # Return True


def main():
    g = {'a': {'b', 'c', 'd'},
          'b': {'a', 'c', 'd', 'f'},
          'c': {'a', 'b', 'd'},
          'd': {'a', 'b', 'c'},
          'e': {'f', 'g'},
          'f': {'b', 'e', 'f'},
          'g': {'e', 'f'}}

    #print("\ng3 = ", g3)

    subGraph={'a', 'b', 'c','d'}
    k=4
    print("\nsubGraph [is "+str(k)+"-clique] = ", subGraph)
    print("---> check_k_clique(subGraph, k="+str(k)+", g=g3) = ", check_k_clique(subGraph, k, g))

if __name__=="__main__":
    main()