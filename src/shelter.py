import csv
from pet import Pet
from dog import Dog
from cat import Cat

class Shelter:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to the shelter."""
        if not isinstance(pet, Pet):
            raise TypeError("Only Pet instances can be added.")
        self.pets.append(pet)

    def list_pets(self):
        """Return a list of all pets in the shelter."""
        return self.pets

    def search_pets_by_type(self, pet_type):
        """Search for pets by type (dog/cat)."""
        if pet_type not in ['dog', 'cat']:
            raise ValueError("Pet type must be 'dog' or 'cat'.")
        return [pet for pet in self.pets if isinstance(pet, Dog if pet_type == 'dog' else Cat)]

    def search_pets_by_breed(self, breed):
        """Search for pets by breed."""
        return [pet for pet in self.pets if pet.get_breed().lower() == breed.lower()]

    def search_pets_by_age(self, age):
        """Search for pets by age."""
        return [pet for pet in self.pets if pet.get_age() == int(age)]

    def adopt_pet(self, name):
        """Adopt a pet from the shelter by name."""
        for pet in self.pets:
            if pet.get_name().lower() == name.lower():
                if pet.is_adopted():
                    print(f"{pet.get_name()} is already adopted.")
                else:
                    pet.set_adopted(True)
                    print(f"{pet.get_name()} has been adopted.")
                return pet
        print(f"No pet named {name} found.")
        return None

    def get_pet_details(self, name):
        """Get detailed information about a pet by name."""
        for pet in self.pets:
            if pet.get_name().lower() == name.lower():
                return pet  # Return the Pet object itself
        print(f"No pet named {name} found.")
        return None

    def save_data(self, filename='data/pets.csv'):
        """Save shelter data to a CSV file."""
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Species', 'Breed', 'Age', 'Adopted', 'Description', 'Notes'])
            for pet in self.pets:
                writer.writerow([
                    pet.get_id(),
                    pet.get_name(),
                    'Dog' if isinstance(pet, Dog) else 'Cat',
                    pet.get_breed(),
                    pet.get_age(),
                    'Yes' if pet.is_adopted() else 'No',
                    pet.get_description(),
                    pet.get_notes()
                ])

    def load_data(self, filename='data/pets.csv'):
        """Load shelter data from a CSV file."""
        self.pets.clear()
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                if len(row) != 8:
                    print(f"Skipping malformed row: {row}")
                    continue
                id, name, species, breed, age, adopted, description, notes = row
                adopted = adopted == 'Yes'
                if species == 'Dog':
                    self.add_pet(Dog(id, name, breed, int(age), description, notes=notes, adopted=adopted))
                elif species == 'Cat':
                    self.add_pet(Cat(id, name, breed, int(age), description, notes=notes, adopted=adopted))
