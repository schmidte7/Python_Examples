g = {'a': {'b', 'c', 'd'},
     'b': {'a', 'c', 'd', 'f'},
     'c': {'a', 'b', 'd'},
     'd': {'a', 'b', 'c'},
     'e': {'g', 'f'},
     'g': {'e', 'f'},
     'f': {'e', 'g'}}

def is_clique(g: dict, k:set):

    for node1 in k: # Iterate through the set (k) below that was an input {'e', 'f', 'g'} Ex. node1 = 'e'
        adj_node1 = g[node1] # If 'e' in in g (dict), then grab the values from that key Ex. adj_node 1 = 'g', 'f'
        for node2 in k: # Iterate through k with a second node Ex. node2 = 'f' then node2 = 'g'
            if node2 not in adj_node1 and node1 != node2: # Ex. If node2 = 'f'/'g' not in adj_node1 (values) and 'e' != 'f'/'g' ????
                #print("node1:", node1)
                #print("node2:", node2)
                return False # Return False since that is not a clique

        return True # Return True since that is a clique


def main():
    print(is_clique(g, {'e', 'f', 'g'}))

if __name__ == "__main__":
    main()