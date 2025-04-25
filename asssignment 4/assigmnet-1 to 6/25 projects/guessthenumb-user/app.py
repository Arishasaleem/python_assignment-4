import random

print(" Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100...")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! 📉 Try again.")
        elif guess > secret_number:
            print("Too high! 📈 Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            break

    except ValueError:
        print("❌ Please enter a valid number.")
        