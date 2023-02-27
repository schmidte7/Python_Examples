# Import packages
from urllib.request import urlopen  # Opens a specific URL and receives the corresponding content
from urllib.parse import quote, urlencode  # Split/combine the URL strings into its components

# Define neighbors function
def neighbors(n: str, c: str, d: float, s: float):
    """Find the neighbors of a (city, country) pair based on the following:
        Neighbors are:
            1. in the same province OR
            2. on the same river or lake OR
            3. on the same sea but at a distance less than s OR
            4. anywhere at a distance less than d
            ...where s and d are given parameters and the distance between ci and cj (two cities) is defined as
                |ci.latitude − cj .latitude| + |ci.longitude − cj .longitude|

        Pre-condition:
        - n (city) needs to be correctly spelled and exist in the real world
        - c (country) needs to be correctly spelled and exist in the real world
        - d (distance 1) is a float value within the string type that needs to be greater than zero. Cannot have negative distances.
        - s (distance 2) is a float value within the string type that needs to be greater than zero. Cannot have negative distances.

        Post-condition:
        -  A list of a set that contains all of the nearest neighbors for that city, country by the specificiations listed in the pre-conditions

        Argument:
        - n(str): The city of interest
        - c(str): The country of interest for that specific city
        - d(float): A specified distance to find X neighbors of that city, country
        - s(float): A specified distance to find X neighbors of that city, country on the same sea

        Return:
        - [{city1, country1}, {city2, country2}, ... {cityx, countryx}] --> A list that contains tuples of the city (n), country (c) within
        a set (removes duplicates, no order)

    """

    # Create a query to pull data on a city's neighbors through specific tables
    # The tables that were used for this project are 'city' and 'located'
    # Outer LEFT JOIN was utilized because data needed to be pulled from the left table ('city') and only match on the right ('location')
    # \'{n}\' and \'{c}\' used to format the query, allowing multi-line strings (no need for line breaks)
    query = f"""
            SELECT c.Name, c.Country
            FROM City c
            LEFT JOIN located l
                ON c.Name = l.City AND c.Country = l.Country
            WHERE
                NOT (c.Name = \'{n}\' AND c.Country = \'{c}\')
                AND ((c.Province IN (SELECT `Province` FROM `City` WHERE `Name` = \'{n}\' AND `Country` = \'{c}\'))
                OR (l.River IN (SELECT `River` FROM `located` WHERE `City` = \'{n}\' AND `Country` = \'{c}\'))
                OR (l.Lake IN (SELECT `Lake` FROM `located` WHERE `City` = \'{n}\' AND `Country` = \'{c}\'))
                OR (l.Sea IN (SELECT `Sea` FROM `located` WHERE `City` = \'{n}\' AND `Country` = \'{c}\')
                    AND (ABS(c.Longitude - (SELECT `Longitude` FROM `City` WHERE `Name` = \'{n}\' AND `Country` = \'{c}\'))
                    + ABS(c.Latitude - (SELECT `Latitude` FROM `City` WHERE `Name` = \'{n}\' AND `Country` = \'{c}\'))) <= {s})
                OR (ABS(c.Longitude - (SELECT `Longitude` FROM `City` WHERE `Name` = \'{n}\' AND `Country` = \'{c}\'))
                    + ABS(c.Latitude - (SELECT `Latitude` FROM `City` WHERE `Name` = \'{n}\' AND `Country` = \'{c}\')) <= {d}))"""

    url = "http://kr.unige.ch/phpmyadmin/query.php?db=mondial&sql=" + quote(
        query)  # Contains the hardcoded URL of the modial database that is
    # encoded by the query string passed as an arguement
    query_results = urlopen(url)  # Open the specified URL from the line prior

    # NOTE: Part of code is utilized from the project document
    neighbors = set()  # Create an empty set called 'neighbors' which does not include duplicates or a specified order
    for line in query_results:  # Iterates through the content line by line from query_results
        string_line = line.decode('utf-8').rstrip()  # Decodes each line by removing trailing whitespaces from each line
        columns = string_line.split(
            '\t')  # Splits the line into a list of columns, which in turn splits a string into a list of substrings
        # at each tab character
        pair = tuple(columns)  # Creates a tuple from the columns
        neighbors.add(pair)  # Adds that tuple to the set 'neighbors'
    query_results.close()

    return list(neighbors)  # Returns the list of tuples within the set

# Use neighbors function recursively to find all reachable cities
def reachable_cities(n: str, c: str, k: int, d: float, s: float):
    """Create a breadth-first search function using neighbors() recursively to find reachable cities from n in 1, 2, ..., k steps.
       Find all the cities reachable from (city,country) in a given number of steps.

        Pre-condition:
        - n (city) needs to be correctly spelled and exist in the real world
        - c (country) needs to be correctly spelled and exist in the real world
        - k (steps) needs to be greater than 0 to get the neighbors of a pair (city, country)
        - d (distance 1) is a string value that needs to be greater than zero. Cannot have negative distances.
        - s (distance 2) is a string value that needs to be greater than zero. Cannot have negative distances.

        Post-condition:
        -  A list that contains tuples of the pairs within a set has all of the nearest neighbors for that city, country by the
        specificiations listed in the pre-conditions

        Arguement:
        - n(str): The city of interest
        - c(str): The country of interest for that specific city
        - k(int): The number of steps the user enters to find the neighbors of the neighbors and so foth
        - d(str): A specified distance to find X neighbors of that city, country
        - s(str): A specified distance to find X neighbors of that city, country on the same sea

        Return:
            - [{city1, country1}, {city2, country2}, ... {cityx, countryx}] --> A list that contains tuples of the city (n), country (c) within
            a set (removes duplicates, no order)

    """

    visited = set()  # Create a set of already visited places
    visited.add((n, c))  # Add starting city so that we do not go back
    queue = []  # Initialize a queue of cities to check

    i = 1  # Initialize Step 1
    while i <= k:  # Stay in the loop while step (i) is less than or equal to k
        if i == 1:  # Only complete this for the first step
            print(str(i) + ' Step--------------------------------------------------\n')
            first_neighbors = neighbors(n, c, d, s)  # Using the function from above, find first neighbors
            print(str(len(first_neighbors)) + ' Cities Reachable:')
            print(first_neighbors)  # Print 'Step 1' reachable cities within their respective country
            visited.update(first_neighbors)  # Add the first neighbors so that they are not visited again
            queue.extend(first_neighbors)  # Add those same pairs to the queue of cities to check
        else:  # If not the first step, complete the following afterwards i = 2 to k:
            print('\n' + str(i) + ' Steps--------------------------------------------------\n')
            new_neighbors = []  # Create a list to become the new queue once the current list (queue) is empty
            while len(queue) > 0:  # While there are still cities in that first queue...
                pop = queue.pop(0)  # Remove one specific city from the queue
                pop_neighbors = neighbors(pop[0], pop[1], d, s)  # Find the neighbors of new city
                for node in pop_neighbors:  # Iterate through each neighbor
                    if node not in visited and len(node) == 2:  # If that node has not been visited and it is a valid set...
                        new_neighbors.append(node)  # Add it to the list for next step's queue
                        visited.add(node)  # Mark the node as visited
            print(str(len(new_neighbors)) + ' Cities Reachable:')  # Print count of cities in each step
            print(new_neighbors)  # Print i Step reachable cities
            queue.extend(new_neighbors)  # Add the new neighbors to the queue for the next step

        i += 1  # Move to next step

# Test Geneva to compare with document's output
reachable_cities('Geneva', 'CH', 5, '2', '4')