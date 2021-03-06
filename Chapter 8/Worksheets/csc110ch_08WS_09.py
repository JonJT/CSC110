# Ws 8_9
# Write a function that takes word of lowercase letters (plaintext) and which returns an enciphered word (cypher text)
# using a circular Caesar cypher for each letter.  Can you upgrade the function for lowercase or upper case 
# Letters?

# The Caesar cipher is one of the earliest known and simplest ciphers. It is a type of substitution cipher in which
# each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1,
# A would be replaced by B, B would become C, and so on.

# If a letter is shifted off the end of the alphabet, it goes back to the beginning of the alphabet.  For example,
# the letter ‘y’ shifted 3 to the right  becomes the letter ‘b’.

# Use appropriate helper functions.

# Now use this function to decipher this encrypted text:


# Zw pfl kvcc kyv kilky, pfl ufe'k yrmv kf ivdvdsvi repkyzex.  – Drib Knrze

from string import ascii_lowercase as lc, ascii_uppercase as uc

def caesar(Ltr, shift):
    if (Ltr in lc):
        return lc[(lc.find(Ltr) + shift) % 26]
    elif (Ltr in uc):
        return uc[(uc.find(Ltr) + shift) % 26]
    else:
        return Ltr

Str = "Zw pfl kvcc kyv kilky, pfl ufe'k yrmv kf ivdvdsvi repkyzex.  – Drib Knrze"

def caesarStr(Str, shift):
    decipherStr = ""
    for Ltr in Str:
        decipherStr += caesar(Ltr, shift)
    return decipherStr

for shift in range(26):
    print(caesarStr(Str, shift))