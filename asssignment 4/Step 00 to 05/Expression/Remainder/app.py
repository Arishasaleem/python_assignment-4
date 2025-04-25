def main():
    divisor : int = int(input("Enter the number you want to div :"))
    divident : int = int(input("Enter the number you want to div with :"))

    quotient : int = divisor // divident
    reminder : int = divisor % divident

    print("The answer of your Qs is :" + str(quotient) , "with the reminder " + str(reminder))

if __name__ == '__main__':
    main()