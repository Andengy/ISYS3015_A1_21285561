# src/pet.py

class Pet:
    def __init__(self, name, breed, age, description):
        self._name = name
        self._breed = breed
        self._age = age
        self._description = description

    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed

    def get_age(self):
        return self._age

    def get_description(self):
        return self._description

    def set_name(self, name):
        self._name = name

    def set_breed(self, breed):
        self._breed = breed

    def set_age(self, age):
        self._age = age

    def set_description(self, description):
        self._description = description

    def __str__(self):
        return f"{self._name} ({self._breed}, {self._age} years old)"

    def detailed_info(self):
        return f"Name: {self._name}\nBreed: {self._breed}\nAge: {self._age} years\nDescription: {self._description}"