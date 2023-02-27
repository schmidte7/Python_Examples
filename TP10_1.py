import csv

def transpose(input_file: str, output_file: str):

    with open(input_file) as infile, open(output_file, 'w', newline = "") as outfile: # Read in the csv output file and set as 'w' for write into it later

        reader = csv.reader(infile) # Iterate through the infile
        writer = csv.writer(outfile) # Iterate through the outfile

        rows = [] # Create empty list to first store the content in the infile
        maxcolumn = 0 # ????

        for line in reader: # Iterate through the infile/reader
            rows.append(line) # Append each line into the created list (should be three lines)
            maxcolumn = max(maxcolumn, len(line)) # 3 items exist (a1,b1,c1)

        for i in range(maxcolumn): # Iterate through the maxcolumn (3)
            transposerow = [] # Create second empty list to store transposed lines
            for j in range(len(rows)): # Iterate through the len(rows) which should be four (4)
                if i < len(rows[j]): # rows[j] = 3 because you are looking at individual 'cells' in rows
                    transposerow.append(rows[j][i]) # Append the position of j and i from rows
            writer.writerow(transposerow) # Write into the output file

def main():
    transpose('Book1.csv', 'Book1-transpose.csv')

if __name__=="__main__":
    main()