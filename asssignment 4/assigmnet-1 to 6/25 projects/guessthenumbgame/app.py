import time

print("Welcome to the Guess the Number Game!")
print("Think of a number between 1 and 100, and I will try to guess it.")
input("Press Enter when you're ready...")

low = 1
high = 100
guesses = 0

while True:
    guess = (low + high) // 2
    guesses += 1
    print(f"\nIs your number {guess}?")
    feedback = input("Type 'h' if my guess is too high, 'l' if it's too low, or 'c' if it's correct: ").lower()

    if feedback == 'c':
        print(f"\nYay! I guessed your number in {guesses} tries! 🎉")
        break
    elif feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    else:
        print("Oops! Please type only 'h', 'l', or 'c'.")

    time.sleep(0.5)
