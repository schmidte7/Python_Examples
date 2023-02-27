import re

def solution(file_path1, file_path2):

    # we open the file reader F1 and the file writer F2
    with open(file_path1, mode="r", encoding="utf-8") as F1, open(file_path2, mode="w", encoding="utf-8") as F2 :

        # the dictionary word_to_lineIndices associates each word/token to the indices of the lines where it appears
        word_to_lineIndices=dict()
        # the dictionary lineIndex_to_line associates each line-index to its corresponding line
        lineIndex_to_line=dict()

        # we set the regular expression used in splitting each line
        reg_exp="[ ,;:\’\"\?!\n\t\r]+"

        # we initialize i, it is the index of each line
        i=0
        # we read the first line in the first file
        line=F1.readline()
        # we set stayInLoop, it will equal to True as long as we have not reached the end of the first file
        stayInLoop=bool(line)
        while stayInLoop :
            # we remove the trailing characters in line
            line=line.rstrip()
            # we associate the line to its index in lineIndex_to_line
            lineIndex_to_line[i]=line
            # we split the line into tokens (words, numbers, etc.) based on the regular expression reg_exp
            tokens=re.split(reg_exp, line)

            # we go through every token in the list tokens
            for token in tokens :
                # we process only non-empty strings (the split function can produce empty strings, i.e. "" is the empty string)
                if len(token)>=1:
                    # if token exists as a key in word_to_lineIndices, then we update the line-indices list where token appears by appending i to it
                    if token in word_to_lineIndices:
                        lineIndices=word_to_lineIndices[token]
                        lineIndices.append(i)

                        # we write token in F2 only if it appears at least two times
                        # the boolean expression len(lineIndices)==2 is used to insure that a token is written only once in F2
                        if len(lineIndices)==2 :
                            F2.write(token+"\n")
                    # else (if token DOESN'T exists as a key in word_to_lineIndices), then we initialize the line-indices list where token appears by setting it to [i]
                    else:
                        word_to_lineIndices[token]=[i]

            # we read the next line from F1
            line=F1.readline()
            # we set stayInLoop, it is equal to True if line is not the end of the first file
            stayInLoop = bool(line)
            # we increment i by 1
            i+=1

    return word_to_lineIndices,lineIndex_to_line


def main():

    file_path1 = "file.txt"
    file_path2 = "file_other.txt"

    print("\nfile_path1 = ", file_path1)
    print("file_path2 = ", file_path2)
    word_to_lineIndex,lineIndex_to_line = solution(file_path1, file_path2)
    for word,lineIndices in word_to_lineIndex.items():
        print("\n\""+word+"\" appears in lines : ")
        for lineIndex in lineIndices:
            line = lineIndex_to_line[lineIndex]
            print("\t", line)


if __name__=="__main__":
    main()



