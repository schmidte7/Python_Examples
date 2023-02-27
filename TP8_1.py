def same_files(file_path1, file_path2, encoding = 'utf-8'):

    with open(file_path1, mode = 'r', encoding=encoding) as f1, open(file_path2, mode = "r", encoding = encoding) as f2: # Open each file1 and file2

        ExitLoop = False # Set statement to False if iterating through file, else True
        while not ExitLoop: # Use while loop because you are dealing with different lenghts (while iterating through...)
            line1 = f1.readline() # Iterate through file1
            line2 = f2.readline() # Iterate through file2
            end_of_file1 = bool(line1) # If the end of file1 is reached, True
            end_of_file2 = bool(line2) # If the end of file2 is reached, True

            if not end_of_file1 and not end_of_file2: # Not at the end of either file
                if line1 != line2: # If their lines are not equal...
                    return False
            elif end_of_file1 and end_of_file2: # Reached the end of the file and not comparable, exit the loop
                return True # Need to use ExitLoop since we use 'return True' later
            else:
                return False # If one of the files is different lengths, return False
    return True # Both files are 100% comparable

def main():
    print("\n----------------------------- Test 1 (same content) ----------------------------------")
    file_path1 = "file1.txt"
    file_path2 = "file2.txt"
    print("file_path1 = ", file_path1)
    print("file_path2 = ", file_path2)
    print("---> same_files(file_path1, file_path2) = ", same_files(file_path1, file_path2))

    print("\n----------------------------- Test 2 (different content) ----------------------------------")
    file_path1 = "file1.txt"
    file_path2 = "file3.txt"
    print("file_path1 = ", file_path1)
    print("file_path2 = ", file_path2)
    print("---> same_files(file_path1, file_path2) = ", same_files(file_path1, file_path2))

if __name__ == "__main__":
    main()