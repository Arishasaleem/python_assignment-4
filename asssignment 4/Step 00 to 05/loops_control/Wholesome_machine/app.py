def affirmation_check():
    affirmation = "I am capable of doing anything I put my mind to."
    print(f"Please type the following affirmation:\n{affirmation}")

    while True:
        user_input = input()
        if user_input.strip() == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation.")
            print(f"Please type the following affirmation:\n{affirmation}")

affirmation_check()
