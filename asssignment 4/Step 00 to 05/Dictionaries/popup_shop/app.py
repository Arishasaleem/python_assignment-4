def fruit_shop():
    fruit_prices = {
        "apple": 3.00,
        "durian": 15.50,
        "jackfruit": 10.00,
        "kiwi": 2.50,
        "rambutan": 5.00,
        "mango": 7.00
    }

    total_cost = 0

    print("\nWelcome to the Fruit Shop!\n")
    
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: ").strip())
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                total_cost += quantity * price
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print(f"\nYour total is ${total_cost:.2f}")

fruit_shop()
