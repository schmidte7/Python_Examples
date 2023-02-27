import pprint #  Provides a capability to “pretty-print” arbitrary Python data structures in a vertical form
import re # Import re for the splitting of words based on punctuation or spacing
import math # Gives access to the underlying C library functions - math.sqrt()

def read_reference_text(filename: str) -> list[list[str]]: # Call in a function that reads in the text reference file
    """
        The first function imports a reference text file that has 100,000 lines. Those lines get individually called into
        a list of sentences within a list that has strings within that inner list. Throughout the function, there are steps
        to remove, replace, and lower the strings (words) of each line.
        - Resource: Project PDF

        Pre-condition:
        - filename points to the correct location
        - filename contains lines ith content (sentences)
        Post-condition:
        - text file is a list of sentences that is broken into a list of words that follows the criteria
        within the code (ex. lowercase, split, etc.)

        Argument:
        -  filename(str): A string that references the location of the text file.

        Returns:
        - list[list[str]] - "text": A list of a list of lines that contains strings (words). The words that are appended to the
        text list are those that are lowercased, '\n', and quotes replaced, and does not include any punctuation.
    """
    f = open(filename, mode = 'r', encoding="utf8")  # Reads ('r') in the text file. Using "utf8" file encoding

    text = [] # Creates an empty list for the output of the read_reference_text() function

    for sentences in f: # Iterates through the lines of sentences within f (text reference file)
        sentences = sentences.lower() # For each word, this operation will lowercase each letter
        sentences = sentences.replace('\n', ' ') # Replaces the new line character with a space
        sentences = sentences.replace('"', ' ') # Replace the quotes with a space
        words = re.split("[ ,;.)'/(!+?:-]", sentences) # Splits the sentences based on the different punctuation marks
        text.append(words) # Appends words within the sentence within a list to create a list of a list of strings
    return text # Returns the text that was originally an empty list
    f.close() # Closed the opened reference text file

text = read_reference_text("ref-sentences.txt")

def make_word_vector(w: str, text: list[list[str]]) -> dict[str, int]:
    """
         This function iterates over each sentence to check if the word appears in that line and returns a dictionary
         with contains the word_list (key) and those words in the sentences and how often they appear (value)
        - Resource: Project PDF

        Pre-condition:
        - text should already be formatted as list[list[str]]
        - w should be included in a word_list (for the example, I just used "Spain")

        Post-condition:
        - Vector contains all words that are in a sentence that contains the w in a {str, int} format

        Arguments:
        - w(str): The word that the dictionary is created for
        - text(list[list[str]]): A list of a list of lines that contains strings (words) that pertain to the w

        Returns:
        - dict[str, int] - "vector": Contains the word w and the amount of times that another word that is not the same
        as w appears in the same line. The int will then count how many times it appears
    """

    # Given stopwords list (Project PDF)
    stopwords = set(
        ["s", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost",
         "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount",
         "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as",
         "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand",
         "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by",
         "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do",
         "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty",
         "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen",
         "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from",
         "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here",
         "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however",
         "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last",
         "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill",
         "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely",
         "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing",
         "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others",
         "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put",
         "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should",
         "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something",
         "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their",
         "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon",
         "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru",
         "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until",
         "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence",
         "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether",
         "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within",
         "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"])

    vector_list = []  # Creates an empty list called vector_list
    for sentence in text: # Iterates through each sentence in the text list
            for word in sentence: # Iterates through each word in the sentence
                if w in sentence: # Looks if w (word_list provided) is in that individual sentence
                    vector_list.append(word) # Appends the word to the vector_list

    vector = {}  # Creates an empty dictionary called vector
    for word in vector_list: # Iterate through each word in the vector_list
        if len(word) >= 3 and word not in stopwords and word !=w: # Does not include words less than three characters, stopwords, or if the word is in the w (ex. "Spain")
            if word in vector: # If the word is in the empty dictionary called 'vector'
                vector[word] = vector[word] + 1 # Add 1 to the value if the key already exists
            else:
                vector[word] = 1 # If the value/key do not exist, add it to the dictionary and add one to the value

    return vector # Returns the dictionary called vector

# Ran tests for dict1 and dict2 to compare with "Spain"
# dict1= make_word_vector('industry',text)
# dict2= make_word_vector('conflict',text)

def sim_word_vec(dict1: dict[str, int], dict2: dict[str, int]) -> float:
    """
        The function computes the scalar product of two dictionaries
        and then computes the cosine similarity of the texts
        - Resource: Sets and Dictionaries (slides 19 to 22)

        Pre-condition:
        - String has to be more than 2 characters and not a stopword
        - Integer >= 0
        Post-condition:
        - Returns a cosine_sim > 0
        - Returns a float value for cosine_sim

        Arguments:
        -  dict1(dict[str,int]): Dictionary that contains one string and the words that appear with that main string with how often it appears
        -  dict2(dict[str,int]): Dictionary that contains one string and the words that appear with that main string with how often it appears

        Returns:
        - float - "cosine_sim": The scalar product of dict1 and dict2
    """

    sp12 = 0.0 # Scalar product of both (1 and 2) dictionaries
    sp_1 = 0.0 # Scalar product of the first (1) dictionary
    sp_2 = 0.0 # Scalar product of the second (2) dictionary
    for word in dict1:
        sp12 += dict1[word] * dict2.get(word, 0)  # Word not in dict2 → 0
        sp_1 += dict1[word] * dict1.get(word,0) # Word not in dict1 → 0
    for word in dict2:
        sp_2 += dict2[word] * dict2.get(word,0) # Word not in dict2 → 0
        cosine_sim = sp12 / (math.sqrt(sp_1 * sp_2)) # Compute cosine similarity
    return cosine_sim

def main():
    """
            The function compares all the word combinations for the test_words and prints the maximum values for each word and their highest similarity.

            Pre-condition:
            - Test of words is included (all lower cased)
            Post-condition:
            - The outcome only contains the number of words that are in the list of test words (example: 12 lines)

            Returns:
            - list - "sim_comparison": Contains the word_test1 and word_test2 words and their cosine similarity value
        """
    #filename = 'ref-sentences.txt'
    #print(read_reference_text(filename))
    #w = "spain"

    # word_list1 includes two fish strings
    word_list1 = ["spain", "anchovy", "france", "internet", "china", "mexico", "fish", "industry", "agriculture",
                 "fishery", "tuna", "transport", "italy", "web", "communication", "labour","fish", "cod"]
    # word_list2 includes one fish string
    word_list2 = ["spain", "anchovy", "france", "internet", "china", "mexico", "fish", "industry", "agriculture",
                 "fishery", "tuna", "transport", "italy", "web", "communication", "labour", "cod"]
    # Contains the list of test words that are to be compared
    words_test = ["canada", "disaster", "flood", "car", "road", "train", "rail", "germany", "switzerland", "technology", "industry", "conflict"]

    # Creates dictionaries for every word that is in the word_test
    word_dict = {word:make_word_vector(word, text) for word in words_test}
    #print(word_dict)

    sim_comparison = [] # Creates an empty list called sim_comparison
    for i in range(len(words_test)): # Iterates over the 12 words in word_test
        max_sim = 0 # Create a max value at 0 to compare to sim_word_vec value
        for j in range(len(words_test)): # An inner loop to iterate over the 12 words in word_test
            if j == i: # If the two words equal one another, do not include in output
                pass
            else:
                sim = sim_word_vec(word_dict[words_test[i]], word_dict[words_test[j]]) # sim to compare to max_sim to override if it is the largest value
                if sim > max_sim: # If sim is greater than max_sim
                    max_sim = sim # Replace what the previous value was before with the new sim
                    j_position = j # Equal j_position to wherever j has iterated through
        print(words_test[i], "->",words_test[j_position], max_sim) # Prints the output of the maximum value between the two dictionary words

   # print(sim_word_vec(dict1, dict2))
    #pprint.pprint(sim_comparison)

if __name__=="__main__":
    main()