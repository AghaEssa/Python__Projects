import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """Returns a list of valid words from the word list file."""
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as inFile:
        wordlist = inFile.read().split()
    print(f"  {len(wordlist)} words loaded.")
    return wordlist

def choose_word(wordlist):
    """Returns a random word from the word list."""
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    """Returns True if all letters of secret_word are in letters_guessed."""
    return all(letter in letters_guessed for letter in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    """Returns a string of the guessed word with underscores for unguessed letters."""
    return ''.join(letter if letter in letters_guessed else '_' for letter in secret_word)

def get_available_letters(letters_guessed):
    """Returns a string of letters that have not been guessed yet."""
    return ''.join(letter for letter in string.ascii_lowercase if letter not in letters_guessed)

def hangman(secret_word):
    """Starts up an interactive game of Hangman."""
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3

    print(f"Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.")

    while guesses_remaining > 0:
        print(f"You have {guesses_remaining} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            warnings_remaining -= 1
            if warnings_remaining < 0:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You lose a guess.")
            else:
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left.")
            continue

        if guess in letters_guessed:
            warnings_remaining -= 1
            if warnings_remaining < 0:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You lose a guess.")
            else:
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left.")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            guesses_remaining -= 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")

        if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations, you won! Your total score is: {guesses_remaining * len(set(secret_word))}")
            return

    print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.")

if __name__ == "__main__":
    print("start")
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman(secret_word)
