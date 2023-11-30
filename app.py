# write 'hello world' to the console
print('hello world')

# let's make a rock paper scissors game, the rules are:
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# the user will be prompted to enter their choice
# the computer will randomly select a choice
# the winner will be determined by the rules above
# The minigame should inform the player whether the player won, lost, or tied with the opponent.
# the user will be prompted if they want to play again
# The minigame should inform the player if the option entered by the player is invalid
# the game should keep track of the score
# the game should end when the player chooses to stop
# the game should print the final score to the console
# start coding

import random

# function to get input from the user and return error if input is not in options array
def get_input( message, options ):
    while True:
        user_input = input(message)
        if user_input.lower in options:
            return user_input
        else:
            print('Invalid input!')


def play_game():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = get_input('Enter your choice (rock, paper, scissors): ', choices)
        computer_choice = random.choice(choices)
        if user_choice == 'rock':
            if computer_choice == 'rock':
                print('You tied!')
            elif computer_choice == 'paper':
                print('You lost!')
                computer_score += 1
            elif computer_choice == 'scissors':
                print('You won!')
                user_score += 1
        elif user_choice == 'paper':
            if computer_choice == 'rock':
                print('You won!')
                user_score += 1
            elif computer_choice == 'paper':
                print('You tied!')
            elif computer_choice == 'scissors':
                print('You lost!')
                computer_score += 1
        elif user_choice == 'scissors':
            if computer_choice == 'rock':
                print('You lost!')
                computer_score += 1
            elif computer_choice == 'paper':
                print('You won!')
                user_score += 1
            elif computer_choice == 'scissors':
                print('You tied!')
        else:
            print('Invalid choice!')
        print(f'Your score: {user_score}')
        print(f'Computer score: {computer_score}')
        play_again = get_input('Play again? (y/n): ', ['y', 'n'])
        if play_again == 'n':
            break
    print(f'Final score: {user_score} - {computer_score}')

play_game()

