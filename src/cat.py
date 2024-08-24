from pet import Pet

class Cat(Pet):
    def __init__(self, id, name, breed, age, description, adopted=False):
        super().__init__(name, breed, age, description)
        self.id = id
        self.adopted = adopted

    def get_id(self):
        return self.id

    def is_adopted(self):
        return self.adopted

    def set_adopted(self, adopted):
        self.adopted = adopted

    def __str__(self):
        return f"{self.get_name()} (Cat, {self.get_breed()}, {self.get_age()} years old, ID: {self.get_id()}, Adopted: {'Yes' if self.is_adopted() else 'No'})"
