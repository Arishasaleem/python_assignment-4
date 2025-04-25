import random

def play_guess():
    secrt_numb = random.randint(1, 99)
    guess_count = 0

    print("i am thinking a number can u guess?Its in 1 to 99")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guess_count += 1

            if guess < 1 or guess > 99:
                print("Please enter a number between 1 and 99.")

                continue

            if guess < secrt_numb:
                print("guess is to low")
        
            elif guess > secrt_numb:
                print("guess to high")

            else:
                print(f"Congo! the numb you guess is {guess_count} tries.The numb was {secrt_numb}")
            break
        
        except ValueError:
          print("❌ Please enter a valid number!")
        

def main():
    while True:
        play_guess()
        play_again = input("🔁 Want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("👋 Thanks for playing! Goodbye!")
            break


if __name__ == '__main__':
    main()