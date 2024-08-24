from pet import Pet

class Cat(Pet):
    def __init__(self, id, name, breed, age, description, adopted=False):
        super().__init__(id, name, breed, age, description, adopted)

    def __str__(self):
        return f"{self.get_name()} (Cat, {self.get_breed()}, {self.get_age()} years old, ID: {self.get_id()}, Adopted: {'Yes' if self.is_adopted() else 'No'})"
