import random
import time

# Words for the game
words = ["python", "java", "javascript", "ruby", "csharp", "php"]

print("="*20)
print("Guess the word")
print("="*20)

while True:
    print("Would you like to play?")
    play = input("Yes or No: ").strip().upper()

    if play == "YES":
        print("Loading...")
        time.sleep(3)

        word = random.choice(words)
        word_length = len(word)

        correct_letters = []
        wrong_letters = []
        attempts = 6  # Number of attempts

        # Function to display the hidden word
        def display_hidden_word():
            hidden_word = ""
            for letter in word:
                if letter in correct_letters:
                    hidden_word += letter
                else:
                    hidden_word += "_"
            return hidden_word

        # Main game loop
        while True:
            # Display the current state of the word
            print("\nWord: " + display_hidden_word())

            # Display wrong letters
            if wrong_letters:
                print("Wrong letters: " + ", ".join(wrong_letters))

            # Ask the player for a letter
            letter = input("Enter a letter: ").lower()

            # Check if the letter is valid
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single valid letter.")
                continue

            if letter in correct_letters or letter in wrong_letters:
                print("You've already tried this letter.")
                continue

            # Check if the letter is in the word and Check if the player has won
            if letter in word:
                correct_letters.append(letter)

                if set(correct_letters) == set(word):
                    print("\nCongratulations! You won. The word was: " + word)
                    break
            else:
                wrong_letters.append(letter)
                attempts -= 1
                print("Incorrect letter. You have {} attempts left.".format(attempts))

            if attempts == 0:
                print("\nYou lost! The word was: " + word)
                break
    elif play == "NO":
        print("Goodbye!")
        break
    else:
        print("Please enter 'Yes' or 'No'.")
