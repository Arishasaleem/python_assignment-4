INCHES_IN_FOOT: int = 12

def main():
    feet : float = float(input("Enter numb you want to find! :"))
    foot : float = feet * INCHES_IN_FOOT

    print("the Inches are :" , foot , "inches")

if __name__ == '__main__':
    main()