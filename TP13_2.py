import numpy

# Intuitively, need to buy first then sell
# Profit = sell(j) - buy(i)
def buy_sell(P):

    max_profit = 0 # Set max_profit to 0 as a starting point

    for i in range(len(P)): # Iterate through the array with i (0)
        for j in range(i+1, len(P)): # Iterate through the array with j (1)
            profit = P[j] - P[i] # To obtain profit, need to substract sell - buy
            if profit > max_profit: # If the profit exceeds max_profit...
                max_profit = profit # Set profit = to max_profit
                sell = j # The position of the day to sell
                buy = i # The position of the day to buy

    return sell, buy, max_profit

def main():
    P = numpy.array([13, 21, 9, 4, 2, 10, 14, 11, 5, 1, 7])
    print(buy_sell(P))

if __name__=="__main__":
    main()