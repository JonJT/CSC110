# WS ch5_8
# Items can be added to a list using the append method:
# L = [] ## empty list
# print(L)
# L.append(2)
# print(L)
# L.append('dog')
# print(L)

# >>> 
# []
# [2]
# [2, 'dog']
# >>> 

# Write a function, sep_ints_and_strgs(L),  which takes a list, L,
# of ints and strings, as a parameter, and which returns 2 lists, one
# containing the ints from L and the other containing the strings
# from L.  Use this function to process the list
# ['dog', 3, 7,2,'cat','5']
# and print out a list of ints and a list of strings.


def sep_ints_and_strgs(L):
    Ints = []
    Strings = []
    for el in L:
        if (type(el) == int):
            Ints.append(el)
        elif (type(el) == str):
            Strings.append(el)
    return Ints, Strings

L = ['dog', 3, 7,2,'cat','5']

print('List', L, 'has the follwing two sublists, ints and strings.')

print(sep_ints_and_strgs(L))