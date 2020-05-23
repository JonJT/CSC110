from random import randint

rolledDice = []
stopList = [4, 6] # set for prime numbers in quiz
roll = randint(1, 6)

while roll not in stopList:
    rolledDice.append(roll)
    roll = randint(1, 6)
rolledDice.append(roll)
print(rolledDice)

# sum is a built in function

