# WS ch7 – 8
# Write a function, guessNum(), where the user tries to guess a secret number 
# between 1 and 128 chosen by computer.  Program tells user guess is too high
# or too low. Score starts at 100 and decreases by 2 for every incorrect guess.
# Use a loop
# while True:
# Print out: final score, secret number, incorrect guesses made,
# congratulatory message if guessed on 1st try.

from random import randint

def guessNum2():
    '''user tries to guess secret number between 1 and 128 chosen by randint.
    Program tells user guess is high/low. Score starts at 100 decreases by 2
    for every incorrect guess. Print out: final score, secret number, incorrect
    guesses made, congratulatory message if guessed on 1st try.'''
    secret = randint(1, 128)
    print('''Welcome to the number guessing game.
    Guess a natural number between 1 and 128. Score
    starts at 100 and dcreases by 2 for every incorrect guess.
    Game over when user guesses secret number.''')
    score = 100
    # guess = 1001
    # choose out of range for 1st try
    # guarantees one time thru loop
    guesses = []
    guess = int(input("What's your guess? "))
    while guess != secret:
        # guess = eval(input("What's your guess? ""))
        guesses.append(guess)
        if guess != secret:
            score -= 2
        if guess < secret:
            print("Your guess is too low.")
        elif guess > secret:
            print("Your guess is too high. ")
        guess = int(input("What's your guess? "))
    print("Your score is ", score)
    print("Secret number is ", secret)
    print("Your incorrect guesses were: ", guesses)
    if len(guesses) == 0:
        print('You guessed the number on the 1st try!')

guessNum2()