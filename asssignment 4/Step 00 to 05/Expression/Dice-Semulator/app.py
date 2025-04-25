import random 

NUM_SIDES = 6


def roll_dice():
    die1 : int = random.randint(1, NUM_SIDES )
    die2 : int = random.randint(5, NUM_SIDES )

    total : int = die1 + die2
    print("The dice numb is " , total)

def main():
    die1 : int = 20
    print("the die is " + str(die1) )
    roll_dice()
    roll_dice()
    roll_dice()
    print("The thrice dice is " + str(die1))   

if __name__ == '__main__':
    main()

    