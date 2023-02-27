import numpy

def duplicates(x):

    for i in range(0,len(x)-1): # Iterate from 0 to len-1 because you do not want to compare i to itself
        for j in range(i+1,len(x)): # Iterate through j but from one position ahead
            if x[i] == x[j]: # If there are two numbers that are equal...
                print("i", i)
                return True # There are duplicates
            else: # If no duplicates were found in the first set of i and j...
                j+=1 # Keep i at its position and move j forward to compare against i
        i+=1 # Once through the end of the list, add one to i to check the next position

    if i >= len(x)-1: # Need to set i/len(x)-1 to a limit OR j/len(x) to show it reached the end
        return False

def duplicates2(x):

    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] == x[j]:
                return True
            else:
                j += 1
    i+=1
    return False

def check_duplicates3(t):
    for i in range(len(t)-1):
        for j in range(i+1,len(t)):
            if t[i] == t[j]:
                return True

    return False

t = numpy.array([2,3,4,5,5])
print(check_duplicates(t))

def main():
    x = numpy.array([2,3,4,5,2])
    print(duplicates(x))
    print(duplicates2(x))

if __name__=="__main__":
    main()


#def duplicates(x):
#    dictionary = dict()
#    numlist = []

#    for number in range(len(x)):
#        numlist.append(number)

#    for number in numlist:
#        if number in dictionary:
#            dictionary[number] = dictionary[number] + 1
#        else:
#            dictionary[number] = 1

#    for key, value in dictionary.items():
#        if value > 1:
#            return True
#        else:
#            return False

#def main():
#    x = [2,3,4,5,4]
#    print(duplicates(x))

#if __name__=="__main__":
#    main()