import random

print('Number guessing Game')

number= random.randint(1, 9)

chances=0

print('Guess a number between 1 and 9:')

while chances < 5:

    guess = int(input('Enter guess:'))

    if(guess == number):
        print('YOU WON (imagine winning)')
        break

    elif guess < number:
        print('Tooooo lowww mate, guess higher than', guess)
    
    else: 
        print('Too high mate, guess a little lower than', guess)

    chances += 1

if not chances < 5:
        print('YOU LOSE!! The number is', number)