# WS ch8_3
# Write a function updown(Word), which for any string prints out what the example below shows if Word = ‘dog’:
# >>> updown(‘dog’)

def updown(word):
    up(word)
    print(word)
    down(word)

def up(word):
    S = len(word)
    for n in range(1, S):
        print(word[:n])
    pass

def down(word):
    S = len(word)
    for n in range(S - 1, 0, -1):
        print(word[:n])
    pass

updown('dog')