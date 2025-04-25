C = int = 299792458  # The speed of light in m/s

def main():
    value_in_kg : float = float(input("The value of kg: "))
    energy_in_joules : float = value_in_kg * (C ** 2)

    print("e = m * C^2...")
    print("m = " + str(value_in_kg) + "kg")
    print("C = " + str(C) + "m/s")

    print(str(energy_in_joules) + "joules in energy")

if __name__ == '__main__':
    main()