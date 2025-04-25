SENTENCE_START: str = "Once upon a time, a "

def main():
    adjective : str = str(input("Please type an adjective and press enter."))
    verb : str = str(input("Please type a verb and press enter."))
    noun : str = str(input("Please type a noun and press enter."))

    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

if __name__ == '__main__':
    main()
