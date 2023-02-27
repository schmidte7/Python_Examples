def perfect_number(n):

    sum = 0 # Set sum at 0 to add divisor later
    d = 1 # The divisor that will divide (n/d)

    # The while loop will stop once n and d are equal ( n=6, d=6)
    while d < n: # While d is less than n (once they equal - perfect number)
        if n % d == 0: # If the remainder is zero (0)
            sum+=d # Add d to the sum
        d+=1 # Add one to the divisor to check the next number

    if sum == n: # If sum and n are equal are some point...
        return True # This means the number is perfect
    else: # If they do not equal
        return False # Return False, not perfect number

def main():
    n = 6
    print(perfect_number(n))

if __name__ == "__main__":
    main()