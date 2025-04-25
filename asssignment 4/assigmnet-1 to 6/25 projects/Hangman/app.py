import random

word_list = ['python', 'developer', 'hangman', 'challenge', 'keyboard', 'function', 'variable', 'typescript']

secret_word = random.choice(word_list)
guessed_letters = []
tries = 6  

print("🎉 Welcome to Hangman!")
print("_ " * len(secret_word))  

while tries > 0:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        print("❌ Wrong guess!")
        tries -= 1

    display_word = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += "_ "

    print(f"\nWord: {display_word}")
    print(f"Lives left: {tries}")

    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

if tries == 0:
    print("\n Game Over! The word was:", secret_word)
