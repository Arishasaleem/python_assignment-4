import random

NUM_ROUNDS = 5
score = 0

print("🎮 Welcome to the High-Low Game!")
print("--------------------------------\n")

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"🔸 Round {round_num}")

    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"👉 Your number is: {your_number}")

    # Ask the user for their guess
    guess = input("Do you think your number is HIGHER or LOWER than the computer's? ").strip().lower()

    # Validate input
    while guess not in ["higher", "lower"]:
        guess = input("❗ Please enter either 'higher' or 'lower': ").strip().lower()

    # Reveal result and update score
    if your_number > computer_number and guess == "higher":
        print(f"✅ You were right! The computer's number was {computer_number}")
        score += 1
    elif your_number < computer_number and guess == "lower":
        print(f"✅ You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"❌ Aww, that's incorrect. The computer's number was {computer_number}")

    print(f"⭐ Your score is now: {score}\n")

print("🎉 Thanks for playing!")
print(f"🏁 Final Score: {score}/{NUM_ROUNDS}")

# End message
if score == NUM_ROUNDS:
    print("🌟 Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("👍 Good job, you played really well!")
else:
    print("🙁 Better luck next time!")
