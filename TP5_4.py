def digits(number):

    if number < 0: # If the value is less than 0, raise Exception or return False
        raise Exception("Value is negative. Please reenter.")
    elif number < 10: # If the number is less than 10, do not need to enter loop. Put inside brackets to look like a list
        return [number]
    else: # If the number isn't negative or less than 10
        decimals = [] # Create empty list

        while number > 0: # While the number is greater than zero because need to check every value
            digits = number % 10 # Assign the remainder of 10 to digits
            decimals.append(digits) # Append digits into the created list
            number = number//10 # To review the next digit, need to divide by 10
        return decimals

def main():
    number = 0
    print(digits(number))

if __name__=="__main__":
    main()