import math

def main():
    ab : float = float(input("Enter the amount of first side :"))
    ac : float = float(input("Enter the amount of second side :"))

    bc : float = math.sqrt(ab**2 + ac**2)

    print("the length of bc is(the hypotenous) is :" + str(bc))

if __name__ == '__main__':
    main()