def select(infile: str, year1: int, year2: int, outfile: str):
    #with open(infile, "r") as FI, open(outfile, "w") as FO:

    FI = open(infile, "r") # Read in a file
    FO = open(outfile, "w") # Write a file
    for line in FI: # Iterate through the read file
        lines = line.strip().split(",") # Extract different parts of the line by splitting by a comma and stripping the whitespaces
        year = int(lines[2]) # Pull year from the read file. Use int to make sure they are the same type
        if year1 <= year and year <= year2: # Year has to be equal or greater than year1 and equal or less than year 2
            FO.write(lines[0]+','+lines[3]+'\r') # Write the file while the positions of (first name[0], country[3])

print('Question 3')
print("test with the parameters 'p1.txt',1950,1959,'p2.txt'")
print('p1.txt =')
print(open('p1.txt','r').read())
select('p1.txt',1950,1959,'p2.txt')
print('output:')
print('p2.txt =')
print(open('p2.txt','r').read())