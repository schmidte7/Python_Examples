import numpy

def maximum(t):
    max = t[0] # Set the first position to maximum
    for i in range(len(t)): # Iterate through the array
        if t[i] > max: # If another array position was larger than before...
            max = t[i] # Assign the higher value to max
    return max # Return the largest value within the array

def main():
    t = numpy.array([5,-17,8,98,5,44,3,-98])
    print(maximum(t))

if __name__ == "__main__":
    main()

