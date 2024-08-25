class Pet:
    def __init__(self, id, name, breed, age, description, adopted=False):
        """
        Initialise a new Pet instance.

        Args:
            id (str): The unique identifier for the pet.
            name (str): The name of the pet.
            breed (str): The breed of the pet.
            age (int): The age of the pet in years.
            description (str): A description of the pet.
            adopted (bool, optional): Whether the pet has been adopted. Defaults to False.
        """
        self._id = id
        self._name = name
        self._breed = breed
        self._age = age
        self._description = description
        self._adopted = adopted

    def get_id(self):
        """Return the unique identifier of the pet."""
        return self._id

    def get_name(self):
        """Return the name of the pet."""
        return self._name

    def get_breed(self):
        """Return the breed of the pet."""
        return self._breed

    def get_age(self):
        """Return the age of the pet in years."""
        return self._age

    def get_description(self):
        """Return the description of the pet."""
        return self._description

    def is_adopted(self):
        """Return whether the pet has been adopted."""
        return self._adopted

    def set_adopted(self, adopted):
        """
        Set the adoption status of the pet.

        Args:
            adopted (bool): Whether the pet has been adopted.
        """
        self._adopted = adopted

    def detailed_info(self):
        """
        Provide detailed information about the pet, vertically aligned.

        Returns:
            str: Detailed information about the pet.
        """
        return (
            f"ID: {self._id}\n"
            f"Name: {self._name}\n"
            f"Breed: {self._breed}\n"
            f"Age: {self._age} years\n"
            f"Description: {self._description}\n"
            f"Adopted: {'Yes' if self._adopted else 'No'}"
        )

    def __str__(self):
        """
        Return a string representation of the pet.

        Returns:
            str: The name, breed, and age of the pet.
        """
        return f"{self._name} ({self._breed}, {self._age} years old)"
