def main():
    number_counts = {}

    while True:
        try:
            num = input("Enter a number (or press Enter to stop): ").strip()
            if not num:
                break
            num = int(num)
            number_counts[num] = number_counts.get(num, 0) + 1
        except ValueError:
            print("Please enter a valid number.")

    print("\nNumber frequencies:")
    for num, count in sorted(number_counts.items()):
        print(f"{num} appears {count} {'time' if count == 1 else 'times'}.")

main()
