import random

NUM_SIDES: int = 6

def main():
    die1 : int = random.randint(1 , NUM_SIDES)
    die2 : int = random.randint(1 , NUM_SIDES)

    total = die1 + die2

    print(f"dice have {NUM_SIDES} sides each.\n"
          f"First die {die1}\n"
          f"Second die {die2}\n"
          f"total is {total}" ) 
    
if __name__ == '__main__':
    main()
