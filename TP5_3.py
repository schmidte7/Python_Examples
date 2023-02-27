import numpy

def shift_to_right(t):
    end = len(t)-1 # Need to start at the end of the array
    aux = t[end] # Set aside the last value to put back into the array later
    i = end # Assign i to end since you want to iterate from the last element in the array

    while i > 0: # Need i to be above 0 since you are iterating backwards
       t[i] = t[i-1] # Set the previous value to the current value (value in postion 3 now in position 4)
       i-=1 # Reduce i by 1 since iterating backwards
    t[0] = aux # Bring back the aux value that you set aside in the beginning

def shift_to_left(s):
    start = 0 # Start at the beginning of the array
    aux = s[start] # Create an aux variable to set aside to add to the end later
    i = start # Start the iterator at the beginning since you iterate forward

    for i in range(0,len(s)-1): # (start, stop) Need to iterate 4 times otherwise out of bounds for number 5
        s[i] = s[i+1] # Set the higher position 1 into position 0, position 2 into 1....
        i+= 1 # Increment i by 1 to get through array
    s[-1] = aux # Set aux = to the last position in the array

def main():
    t = numpy.array([1,2,3,4,5])
    print(shift_to_right(t))
    print("Shifted to the right:", t)

    s = numpy.array([1, 2, 3, 4, 5])
    print(shift_to_left(s))
    print("Shifted to the left:", s)

if __name__=="__main__":
    main()





