def main():

    fahrenheit = float(input("Enter temperature in Fahrenheit:"))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"temperature:{fahrenheit}F = {celsius}C")


if __name__ == '__main__':
    main()