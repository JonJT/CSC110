# WS ch8_6B
# Write a function, longestWordIn(String), which returns the length of the longest
# word in String and the corresponding word(s).  

def longestWordIn(String):
    lOfWords = String.split()
    lOfLen = []
    for Word in lOfWords:
        lOfLen.append(len(Word))
    mxLen = max(lOfLen)
    lOfWordsMxLen = []
    for Word in lOfWords:
        if len(Word) == mxLen:
            lOfWordsMxLen.append(Word)
    return mxLen, lOfWordsMxLen