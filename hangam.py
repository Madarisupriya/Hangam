import random

# Small list of predefined words
words = ["apple", "tiger", "house", "table", "robot"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=== HANGMAN GAME ===")

while wrong_guesses < max_wrong_guesses:
    # Display the word
    display += ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the player has guessed the word
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        guessed_letters.append(guess)
        wrong_guesses += 1
        print("Wrong!")
        print("Remaining guesses:", max_wrong_guesses - wrong_guesses)

# If player loses
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", word)