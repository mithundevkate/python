'''
Test 2: Any language (3/20)
Solve the game "Guess a number", find a secret integer between 1 and 1000000
in less than 50 guesses. Write a function that solves the game without user input and returns the
solution by using the function verify() which is defined with the following
specification:
function verify(guess: integer) -> integer
Argument:
     guess (integer) the number to verify
Returns:
     0 if the guess is the solution, your program won
     -1 if the solution is smaller than the guess parameter
     1  if the solution is bigger than the guess parameter'''

import random
def verify(guess_num):

    attemps = 0
    rand_num = random.randint(1,1000000)
    while attemps != 50:
        if  guess_num == rand_num:
            print(0)
            break
        elif rand_num < guess_num:
            print(-1)
        elif rand_num > guess_num:
            print(1)

        attemps = attemps + 1
       
verify(guess_num = random.randint(1,1000000))
