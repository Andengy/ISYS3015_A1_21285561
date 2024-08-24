class Pet:
    def __init__(self, id, name, breed, age, description, adopted=False):
        self._id = id
        self._name = name
        self._breed = breed
        self._age = age
        self._description = description
        self._adopted = adopted

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed

    def get_age(self):
        return self._age

    def get_description(self):
        return self._description

    def is_adopted(self):
        return self._adopted

    def set_adopted(self, adopted):
        self._adopted = adopted

    def __str__(self):
        return f"{self._name} ({self._breed}, {self._age} years old, ID: {self._id}, Adopted: {'Yes' if self._adopted else 'No'})"

    def detailed_info(self):
        return f"Name: {self._name}\nBreed: {self._breed}\nAge: {self._age} years\nDescription: {self._description}\nAdopted: {'Yes' if self._adopted else 'No'}"
