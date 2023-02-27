def prime(n):

    i = 1 # Do not start at 0
    count = 0 # Need a counter to get the first n of prime numbers

    while count < n: # Stops iterating once count and n are equal
        res = True # Set res = True if that number is prime
        if i == 1: # 1 is not a prime number
            res = False
        elif i == 2: # 2 is a prime number
            res = True
        else:
            d = 2 # Start at 2, and this will increase d to check if it's divisble by 3, 4...10
            while d < i and res == True: # While d is less than i, meaning it cannot be divided by itself
                if i % d == 0: # If the remainder is 0, then it is not a prime
                    res = False
                else: # If the remainder is 1
                    d+=1 # Add one to d and go through second while loop again (i = 3) (F and T = T)

        if res == True: # 3 would not be less than 3 but is res == True
            print(i) # Print the second i (2, 3)
            count+=1 # Add one to the counter
        i+=1 # Once done with a counter or if the number is not prime, add one to i to check the next

def main():
    n = 4
    print(prime(n))
if __name__=="__main__":
    main()