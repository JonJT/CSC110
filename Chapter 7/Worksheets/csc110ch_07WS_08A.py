# WS ch7 – 8A
# Write a function, rollUntilSnkEyes() that rolls a 6-sided dice
# 2 times, & stops when both are ones, SNAKE EYES.
# Score starts at 1000, every roll of the 2 dice
# that does not produce 1 and 1 debits score by 5
# Print out the final score & all rolls made.  Computer rolls the
# dice using the random module.  Uses a while loop.

from random import randint

def roll2Dice():
    l = []
    for r in range(2):
        roll = randint(1, 6)
        l.append(roll)
    return l


def rollUntilSnkEyesB():
    score = 1000
    rollsMade = []
    roll = roll2Dice()
    while sum(roll) != 2:
        rollsMade.append(roll)
        roll = roll2Dice()
        score -= 5
    rollsMade.append(roll)
    print(score)
    print(rollsMade)

rollUntilSnkEyesB()

def rollUntilSnkEyes():
    score = 1000
    rollsMade = []
    while True:
        DR = roll2Dice()
        rollsMade.append(DR)
        sumDR = sum(DR)
        if (sumDR == 2):
            break
        else: # snake eyes not rolled
            score -= 5
    print("Final score is:", score)
    print("Rolls made:")
    print(rollsMade)

# rollUntilSnkEyes()