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

    def detailed_info(self):
        """Provides detailed information vertically aligned."""
        return (
            f"ID: {self._id}\n"
            f"Name: {self._name}\n"
            f"Breed: {self._breed}\n"
            f"Age: {self._age} years\n"
            f"Description: {self._description}\n"
            f"Adopted: {'Yes' if self._adopted else 'No'}"
        )

    def __str__(self):
        return f"{self._name} ({self._breed}, {self._age} years old)"
