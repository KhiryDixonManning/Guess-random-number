import random

def guess(x):
    random_number = random.randint(1, x)
    while True:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print('Sorry, try again. Too low.')
            elif guess > random_number:
                print('Sorry, try again. Too high.')
            else:
                print(f'Yay, nice work!! You have guessed the number {random_number} correctly')
                break
        except ValueError:
            print("Please enter a valid integer.")

def computer_guess(x):
    low = 1
    high = x
    print(f"Think of a number between 1 and {x}")
    
    while True:
        if low == high:
            guess = low
        else:
            guess = random.randint(low, high)
        
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f'Yay! The computer guessed correctly, it was {guess}')
            break
        
        if low > high:
            print("Something went wrong. The number cannot be found.")
            break

# Uncomment the function you want to play
# guess(1000)
# computer_guess(1000)