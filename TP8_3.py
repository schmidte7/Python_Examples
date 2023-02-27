def inverse_dictionary(person_to_age):

    age_to_people = dict() # Create new dictionary

    for person, age in person_to_age.items(): # Iterate through the first dictionary
        if age in age_to_people: # If the new key is in the new dictionary
            people = age_to_people[age] # Set the values to people and key is age
            people.add(person) # Add to the set that is created below
        else: # If age is not in the new dictionary
            age_to_people[age] = set([person]) # Add the key and value as a set to add mutliple, no dupe people
                                               # Remember to use ([]) for sets!!!!
    return age_to_people

def main():
    person_to_age = {"Mary": 25, "Karl": 35, "James": 20, "Stacy": 25, "Johanna": 37, "Ari": 35}
    print("\nperson_to_age = ", person_to_age)
    print("---> inverse_dictionary(person_to_age) = ", inverse_dictionary(person_to_age))

if __name__ == "__main__":
    main()