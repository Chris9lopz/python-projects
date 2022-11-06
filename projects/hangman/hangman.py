# Import modules
import random
from hangman_art import logo
from hangman_art import stages
from hangman_wordlist import word_list

# Create a hangman game

# Call variable logo in hangman_art module
print(logo)

# Call a list of posible words from hangman_wordlist 
# Select a random word from the list
chosen_word = random.choice(word_list)

# Create a empty list 
blank_list = []

# Add into the empty list the length of the chosen word
for i in range(len(chosen_word)):
    blank_list.append("_")

end_of_game = False
lives = 6

# Loop until is not '_' more in the blank_list or blank_list equal to 0
while not end_of_game:
    
    # Ask to the user a letter and convert in a lower letter
    guess = input("Guess a letter: ").lower()

    # Modify the value of the blank list if the letter is in chosen_word
    for position in range(len(blank_list)):
        letter = chosen_word[position]
        if letter == guess:
            blank_list[position] = letter
    
    if guess not in blank_list:
        print(stages[lives])
        lives -= 1
        if lives < 0:
            end_of_game = True
            print(f'The word was {chosen_word}')
            print('You lose')
        

    print(f"{' '.join(blank_list)}\n")
    
    if '_' not in blank_list:
        print('You won')
        end_of_game = True

