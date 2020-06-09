# Ws ch8_6
# Write a function, num_words_in(Sentence), which returns the number of words in Sentence.

def num_words_in(Sentence):
    # counter = 0
    # for word in Sentence.split():
    #         counter += 1
    # return counter
    return len(Sentence.split())

Sentence = "hello there how are you"

print(num_words_in(Sentence)) # should return 5