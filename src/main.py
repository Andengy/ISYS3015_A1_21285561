from shelter import Shelter
from dog import Dog
from cat import Cat

def display_main_menu():
    print("=== Welcome to the Pet Adoption System ===")
    print("+++ Please Press '7' to load data before continuing +++")
    print("1. List all pets")
    print("2. Add a new pet")
    print("3. Search for a pet")
    print("4. Adopt a pet")
    print("5. Display pet details")
    print("6. Save shelter data")
    print("7. Load shelter data")
    print("8. Exit")

def add_pet(shelter):
    pet_type = input("Enter pet type (dog/cat): ").lower()
    id = input("Enter pet ID: ")
    name = input("Enter pet's name: ")
    breed = input("Enter breed: ")
    age = input("Enter age: ")
    description = input("Enter description: ")
    notes = input("Enter any special notes about the pet: ")

    if pet_type == 'dog':
        new_pet = Dog(id, name, breed, int(age), description, notes=notes)
    elif pet_type == 'cat':
        new_pet = Cat(id, name, breed, int(age), description, notes=notes)
    else:
        print("Invalid pet type.")
        return

    shelter.add_pet(new_pet)
    print(f"{name} the {pet_type} has been added to the shelter.")

def list_pets(shelter):
    pets = shelter.list_pets()
    if not pets:
        print("No pets available.")
    else:
        print("=== All Pets in the Shelter ===")
        for pet in pets:
            print(pet)

def search_pets(shelter):
    search_option = input("Search by: 1. Type 2. Breed 3. Age\nEnter your choice (1-3): ")
    if search_option == '1':
        pet_type = input("Enter pet type (dog/cat): ").lower()
        results = shelter.search_pets_by_type(pet_type)
    elif search_option == '2':
        breed = input("Enter breed: ")
        results = shelter.search_pets_by_breed(breed)
    elif search_option == '3':
        age = input("Enter age: ")
        results = shelter.search_pets_by_age(age)
    else:
        print("Invalid choice.")
        return

    if results:
        for pet in results:
            print(pet)
    else:
        print("No pets found matching your criteria.")

def adopt_pet(shelter):
    name = input("Enter the name of the pet to adopt: ")
    adopted_pet = shelter.adopt_pet(name)
    if adopted_pet:
        print(f"Congratulations! You've adopted {adopted_pet.get_name()}.")
    else:
        print("Pet not found.")

def display_pet_details(shelter):
    while True:
        name = input("Enter the pet's name: ")
        pet = shelter.get_pet_details(name)
        if pet:
            print(pet.detailed_info())
            action = input("Type 'adopt' to proceed with adoption, 'details' to view another pet, or 'menu' to return to the main menu: ").lower()
            if action == 'adopt':
                adopt_pet(shelter)
                break
            elif action == 'details':
                continue
            elif action == 'menu':
                break
            else:
                print("Invalid choice, returning to main menu.")
                break
        else:
            print("Pet not found. Returning to the main menu.")
            break

def save_shelter_data(shelter):
    shelter.save_data()
    print("Shelter data saved successfully.")

def load_shelter_data(shelter):
    shelter.load_data()
    print("Shelter data loaded successfully.")

def main():
    shelter = Shelter()

    while True:
        display_main_menu()
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            list_pets(shelter)
        elif choice == '2':
            add_pet(shelter)
        elif choice == '3':
            search_pets(shelter)
        elif choice == '4':
            adopt_pet(shelter)
        elif choice == '5':
            display_pet_details(shelter)
        elif choice == '6':
            save_shelter_data(shelter)
        elif choice == '7':
            load_shelter_data(shelter)
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
