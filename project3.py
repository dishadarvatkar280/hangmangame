import random
import hangman_words
import hangman_art

# Display the Hangman game logo at the start
print(hangman_art.logo)

# Use the word list from hangman_words.py file
word_list = hangman_words.word_list

# Set initial number of lives
lives = 6

# Get the hangman stages (visual representation)
stages = hangman_art.stages

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Create a placeholder for the word using underscores
placeholder = "_" * len(chosen_word)

# Show the hidden word initially
print("Word to guess: " + placeholder)

# Flag to control game loop
game_over = False

# To keep track of all correctly guessed letters
correct_letters = []

while not game_over:

    # Show how many lives are left (user-friendly message)
    print(f"****************************<???>/{lives} LIVES LEFT****************************")

    # Take the user's guess as input and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    # Inform the user if they've already guessed this letter
    if guess in correct_letters:
        print(f"You have entered the same letter '{guess}' already. Life won't be deducted for this!")

    display = ""

    # Loop to check each letter in the word and update the placeholder
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Show the current progress of the word
    print("Word to guess: " + display)

    # Inform user if their guess is wrong and reduce a life
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word... You lose a life!")

        # If no lives left, end the game and reveal the word
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The correct word was: {chosen_word}")

    # If the word has been guessed completely, the user wins
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        won=hangman_art.logo2
    # Show the current hangman stage from the stages list
    print(stages[lives])
