
''' slow version, because we read (at each iteration) the (i-1)-th or (i+1)-th item in the list (it goes through i or i+1 elements) '''
def word_context__2(text, w):
    candidateContext_to_count = dict()

    len_text=len(text)
    for i in range(0, len(text)):
        if text[i] == w :
            if i>0 :
                if text[i-1] in candidateContext_to_count :
                   candidateContext_to_count[text[i-1]]=candidateContext_to_count[text[i-1]] + 1
                else:
                    candidateContext_to_count[text[i-1]]=1

            if i+1<len_text :
                if text[i+1] in candidateContext_to_count :
                   candidateContext_to_count[text[i+1]] = candidateContext_to_count[text[i+1]]+1
                else:
                    candidateContext_to_count[text[i+1]] = 1

    result = set()
    for candidateContext, count in candidateContext_to_count.items():
        if count >= 3:
            result.add(candidateContext)

    return result


''' fast/efficient version, we avoid the ineffeciency described in the previous version '''
def word_context(text, w):
    # the dictionary candidateContext_to_count will store the number of times a given string appears before or after w
    candidateContext_to_count=dict()

    current_str=None # current_str will point on the current string
    next_str=None    # next_str will point on the next string (the string after current_str)
                     # previous_str below will point on the previous string (the string before current_str)

    for str in text :
        previous_str=current_str
        current_str=next_str
        next_str=str

        if w==current_str :
            if previous_str is not None :
                if previous_str in candidateContext_to_count:
                    candidateContext_to_count[previous_str]=candidateContext_to_count[previous_str]+1
                else:
                    candidateContext_to_count[previous_str] =1

            if next_str is not None :
                if next_str in candidateContext_to_count:
                    candidateContext_to_count[next_str]=candidateContext_to_count[next_str]+1
                else:
                    candidateContext_to_count[next_str]=1

    result=set()
    for candidateContext, count in candidateContext_to_count.items():
        if count>=3 :
            result.add(candidateContext)

    return result

def main():

    text=["a", "linear", "function", "is", "a", "function", ".", "Each", "linear", "function", "has", "a", "straight", "line",
            "graph", ".", "The", "addition", "of", "a", "linear", "function", "and", "another", "linear", "function", "is", "linear",
            ".", "In", "linear", "algebra,", "a", "linear", "function", "is", "a", "linear", "map"]

    w = "function"
    # w = "linear"

    print("\ntext = ", text)
    print("w = ", w)
    print("---> [fast version] word_context(text, w)    = ", word_context(text, w))
    print("---> [slow version] word_context__2(text, w) = ", word_context__2(text, w))

if __name__ == "__main__":
    main()