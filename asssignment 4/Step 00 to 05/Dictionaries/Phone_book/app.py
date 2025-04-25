def phonebook_app():
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            number = input("Enter phone number: ").strip()
            phonebook[name] = number
            print(f"Contact saved: {name} → {number}")

        elif choice == "2":
            name = input("Enter name to search: ").strip()
            if name in phonebook:
                print(f"{name}'s number: {phonebook[name]}")
            else:
                print(f"{name} not found in phonebook.")

        elif choice == "3":
            if phonebook:
                print("\nPhonebook Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty.")

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            if name in phonebook:
                del phonebook[name]
                print(f"Deleted {name} from phonebook.")
            else:
                print(f"{name} not found.")

        elif choice == "5":
            print("Exiting phonebook. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

phonebook_app()
