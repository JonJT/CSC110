# CSC 110 Spring 2020  Quiz 5 Take-home                       NAME: Jonathan Tally
# Write clear, legible code, the simpler the better. Make sure your code works.   Due Monday at class start.  
# Use the editor to write your code. Submit a file, Quiz_5_YourFullName.py in an email that has as subject 
# csc 110 quiz 5_YourFullName.   Points will be deducted if submission is late.   

# Uppercase letters can be used in Booleans.  For all uppercase letters,  ‘A’ < ‘B’ < ‘C’ < … < ‘x’ < ‘Y’ < ‘Z’.  For example, 
# >>> 'O' < 'P'
# True
# >>> 'F' > 'G'
# False
# >>> 

#  1. [20 pts] Write a function, LtrValue(Ltr), which returns the value a single element string, Ltr,  as follows:
#     any single letter of   'A'  through  'G', inclusive,  has value of 10
#     any single letter of  'H'  through  'N', inclusive,   has value of 20
#     any single letter of  'O' through  'U', inclusive,   has value of 30
#     any single letter of  'V'  through 'Z', inclusive,  has value of  40
#     Anything else for Ltr (lowercase letter, number, punctuation, etc.) has value   0.
# Hint: To determine the value of Ltr, use Booleans like the ones shown below to compute the value of any uppercase letter:
# >>> 'A' <= 'C' <= ‘G'
# True
# >>> 'A' <= 'Q' <= ‘G'
# False
# Sample run:

# for Ltr in 'ADG iHL-N':
#     print(Ltr,'has value',LtrValue(Ltr))
# A has value 10
# D has value 10
# G has value 10
#   has value 0
# i has value 0
# H has value 20
# L has value 20
# - has value 0
# N has value 20

# The sample run also shows how to traverse a string a single string at a time.

def LtrValue(Ltr):
    if ('A' <= Ltr <= 'G'):
        return 10
    elif ('H' <= Ltr <= 'N'):
        return 20
    elif ('O' <= Ltr <= 'U'):
        return 30
    elif ('V' <= Ltr <= 'Z'):
        return 40
    else:
        return 0


# 2. [20 pts] Write a function,  WordValue(Word), which returns the value of Word as
# the sum of the values it its letters.  Uses the function from  Q1 as a helper function.
# Sample Run:
# for Word in ['ABE',’OPRA','OPRA-JONES']:
#     print(Word,'has value',WordValue(Word))

# ABE has value 30
# OPRA has value 100
# OPRA-JONES has value 210


def WordValue(Ltrs):
    Sum = 0
    for Ltr in Ltrs:
        Sum += LtrValue(Ltr)
    return Sum


words = ['ABE','OPRA','OPRA-JONES']
for word in words:
    print(word,'has value',WordValue(word))


# 3 .[20 pts] Write a function, ListOfWordsSumProd(LOfWords), where LOWords is a  list of words, which returns the sum of 
# the values of the words and the product of the values of the words in the list, LOfWords.  Use the previous function as a helper function.
# Sample run:

# For the full name ['ABE', 'OPRA', 'OPRA-JONES']:
#      The sum of the values of the words is 340
#      The product of the values of the words is 630000

def ListOfWordsSumProd(Ltrs, Ltrs):
    Sum = 0
    for word in LOWrods:
        Sum += WordValue(word)
    Prod = 1
    for word in LOWrods:
        Prod *= WordValue(word)
    return Sum, Prod
        

LOWrods = ['ABE', 'OPRA', 'OPRA-JONES']
print(ListOfWordsSumProd(LOWrods))


#### This as far as I'm able to get with any one part working. I reached out to a friend of mine that has been working at Amazon as a senior dev for years and has a
# CompSci degree. He helped walk me through with the following solutions that I understand better.

# def LtrValue(Ltr):
#     if ('A' <= Ltr <= 'G'):
#         return 10
#     elif ('H' <= Ltr <= 'N'):
#         return 20
#     elif ('O' <= Ltr <= 'U'):
#         return 30
#     elif ('V' <= Ltr <= 'Z'):
#         return 40
#     else:
#         return 0

# def WordValue(Ltrs):
#     Sum = 0
#     for Ltr in Ltrs:
#         Sum = Sum + LtrValue(Ltr)
#     return Sum

# words = ['ABE','OPRA','OPRA-JONES']
# for word in words:
#     print(word,'has value',WordValue(word))
    
# def SumValues(Words):
#     Sum = 0
#     for word in Words:
#         Sum += WordValue(word)
#     return Sum

# def ProdValues(Words):
#     Prod = 1
#     for word in Words:
#         Prod *= WordValue(word)
#     return Prod
    
# print("The sum of the values of the words is ", SumValues(words))
# print("The product of the values of the words is ", ProdValues(words))

# ###################################################################

# def LtrValue(Ltr):
#     if ('A' <= Ltr <= 'G'):
#         return 10
#     elif ('H' <= Ltr <= 'N'):
#         return 20
#     elif ('O' <= Ltr <= 'U'):
#         return 30
#     elif ('V' <= Ltr <= 'Z'):
#         return 40
#     else:
#         return 0

# def WordValue(Ltrs):
#     Sum = 0
#     for Ltr in Ltrs:
#         Sum = Sum + LtrValue(Ltr)
#     return Sum

# words = ['ABE','OPRA','OPRA-JONES']
# for word in words:
#     print(word,'has value',WordValue(word))
    
# def SumValues(Words):
#     Sum = 0
#     for word in Words:
#         Sum += WordValue(word)
#     return Sum

# def ProdValues(Words):
#     Prod = 1
#     for word in Words:
#         Prod *= WordValue(word)
#     return Prod
    
# print("The sum of the values of the words is ", SumValues(words))
# print("The product of the values of the words is ", ProdValues(words))

# class Data:
#     def __init__(self, wordSum, wordProd):
#         self.sum = wordSum
#         self.prod = wordProd

# def DoItTheWrongWay(Words):
#     returnData = Data(0,1)
    
#     for word in Words:
#         returnData.sum += WordValue(word)
#         returnData.prod *= WordValue(word)
#     return returnData
    
# data = Data(DoItTheWrongWay(words))

# print("The sum of the values of the words is ", data.sum)
# print("The product of the values of the words is ", data.prod)


# 4.  [10 pts]Using  your full name,  all in uppercase letter,  from the class roster, use the function from Q3 to evaluate 
# the product of the values of your names divided by the sum of the values of your names.
# Print out a labelled answer to this question (follow same format as sample run) and express the answer to 2 decimal places.
# Sample run:

# For the name ['ABE', 'OPRA', 'OPRA-JONES'] :
#     (product of name values)/(sum of name values) =  1852.94





# To Submit:
# Your quiz .py file, csc110_Quiz_5_YourFullName.py in an email that has as subject csc110_Quiz_5_YourFullName.
# 2.  In your file, put a youtube link of a video showing and discussing Q1, paying particular attention to how you did a 
# hand selection of qualifying ints  from 20 to 40, inclusive . Use https://screencast-o-matic.com/ to download a video creation application.   
# I need to see Python code on the screen and to hear your voice as you explain.  Be sure to announce yourself at the beginning of the video.  


