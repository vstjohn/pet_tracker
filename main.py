pets = []
feedings = []

def clean_title(text):
    return text.strip().title()

def greet_user():
    name = input("Whats is your name? ")
    print("Welcome to Pet Tracker,", name)

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Add a pet")
    print("2. View pets")
    print("3. Log feeding")
    print("4. View feedings")
    print("5. Exit")

def add_pet():
    pet_name = clean_title(input("Enter your pet's name: "))
    species = clean_title(input("Enter your pet's species: "))
    pet = {"name": pet_name, "species": species}
    pets.append(pet)
    print(pet_name, "has been added!")

def view_pets():
    if len(pets) == 0:
        print("There are no pets!")
    else:
        print("Your pets:")
        for pet in pets:
            print("-", pet["name"], "(" + pet["species"] + ")")

def pick_pet_name():
    if len(pets) == 0:
        print("No pets yet!")
        return None

    print("Choose a pet:")
    for i, pet in enumerate(pets, start=1):
        print(f"{i}. {pet['name']} ({pet['species']})")

    choice = input("Enter number: ").strip()
    if not choice.isdigit():
        print("Please enter a number.")
        return None

    idx = int(choice) - 1
    if idx < 0 or idx >= len(pets):
        print("That number is not in the list.")
        return None

    return pets[idx]["name"]

def log_feeding():
    pet_name = pick_pet_name()
    if pet_name is None:
        return

    food = input("What did you feed them? ").strip()
    feeding = {"pet": pet_name, "food": food}
    feedings.append(feeding)
    print("Logged")

def view_feedings():
    if len(feedings) == 0:
        print("No feedings logged yet.")
    else:
        print("Feeding history:")
        for f in feedings:
            print("-", f.get("pet", "UNKNOWN"), "was fed", f.get("food", "UNKNOWN"))

def handle_choice(choice):
    if choice == "1":
        add_pet()
    elif choice == "2":
        view_pets()
    elif choice == "3":
        log_feeding()
    elif choice == "4":
        view_feedings()
    elif choice == "5":
        print("Goodbye!")
        return False
    else:
        print("Invalid choice. Try again.")
    return True

greet_user()

running = True
while running:
    show_menu()
    choice = input("Enter your choice: ")
    running = handle_choice(choice)