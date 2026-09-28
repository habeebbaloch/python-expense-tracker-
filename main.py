import os

# Create files if they don't exist
if not os.path.exists("data.txt"):
    open("data.txt", "w").close()

if not os.path.exists("date.txt"):
    with open("date.txt", "w") as f:
        f.write("Sep,2026")


def setting():
    print("-"*10, "SETTING", "-"*10)

    year = input("Enter year: ")
    month = input("Enter month: ")

    with open("date.txt", "w") as f:
        f.write(f"{month},{year}")

    print("Date updated ✅")
    main_menu()


def main_menu():
    print("\n" + "-"*10, "MAIN MENU", "-"*10)
    print("1. Add expenses")
    print("2. Remove expense")
    print("3. Check total spend")
    print("4. Total")
    print("5. Setting")
    print("6. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter only numbers.")
        return main_menu()

    if choice == 1:
        add_expenses()
    elif choice == 2:
        remove_expenses()
    elif choice == 3:
        total_spend()
    elif choice == 4:
        total()
    elif choice == 5:
        setting()
    elif choice == 6:
        print("GOOD BYE 👋")
    else:
        print("Invalid choice.")
        main_menu()


def add_expenses():
    print("-"*10, "ADD EXPENSES", "-"*10)

    try:
        amount = float(input("Enter amount (PKR): "))
    except ValueError:
        print("Enter amount in numbers.")
        return add_expenses()

    date = input("Enter date: ")
    category = input("Enter category: ").lower()

    with open("data.txt", "a") as f:
        f.write(f"{date},{category},{amount}\n")

    print("Expense added ✅")
    main_menu()


def total_spend():
    print("-"*10, "TOTAL SPEND", "-"*10)

    month = "Sep"
    year = "2026"

    try:
        with open("date.txt", "r") as f:
            parts = f.read().strip().split(",")
            if len(parts) == 2:
                month, year = parts
    except FileNotFoundError:
        pass

    found = False

    with open("data.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue

            found = True
            date, category, amount = parts

            print(f"Date: {date}/{month}/{year}")
            print(f"{category}: PKR {amount}")
            print("-"*25)

    if not found:
        print("No expenses found.")

    main_menu()


def remove_expenses():
    print("-"*10, "REMOVE EXPENSES", "-"*10)

    category = input("Enter category: ").lower()
    date_input = input("Enter date: ")

    new_data = []
    removed = False

    with open("data.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue

            date, saved_category, amount = parts

            if saved_category == category and date == date_input:
                removed = True
            else:
                new_data.append(line)

    with open("data.txt", "w") as f:
        f.writelines(new_data)

    if removed:
        print("Record removed ✅")
    else:
        print("Record not found.")

    main_menu()


def total():
    print("-"*10, "TOTAL", "-"*10)

    total_amount = 0
    found = False

    with open("data.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue

            found = True
            date, category, amount = parts

            print(f"Date: {date}")
            print(f"{category}: PKR {amount}")
            print("-"*20)

            total_amount += float(amount)

    if not found:
        print("No expenses found.")

    print(f"Total: PKR {total_amount}")
    main_menu()


main_menu()
