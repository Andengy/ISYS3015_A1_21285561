import pytest
from src.pet import Pet

def test_pet_initialization():
    # Create a Pet instance
    pet = Pet(id="1", name="Buddy", breed="Golden Retriever", age=3, description="Friendly", adopted=False)

    # Assert that all attributes are correctly initialized
    assert pet.get_id() == "1"
    assert pet.get_name() == "Buddy"
    assert pet.get_breed() == "Golden Retriever"
    assert pet.get_age() == 3
    assert pet.get_description() == "Friendly"
    assert not pet.is_adopted()

def test_pet_adoption():
    # Create a Pet instance
    pet = Pet(id="2", name="Whiskers", breed="Siamese", age=2, description="Playful", adopted=False)
    
    # Mark the pet as adopted
    pet.set_adopted(True)
    
    # Assert that the pet is now marked as adopted
    assert pet.is_adopted()

def test_pet_detailed_info():
    # Create a Pet instance
    pet = Pet(id="3", name="Max", breed="Labrador", age=5, description="Loyal", adopted=True)
    
    # Get detailed information about the pet
    detailed_info = pet.detailed_info()
    
    # Define expected detailed information
    expected_info = (
        "ID: 3\n"
        "Name: Max\n"
        "Breed: Labrador\n"
        "Age: 5 years\n"
        "Description: Loyal\n"
        "Adopted: Yes"
    )
    
    # Assert that the detailed information is correct
    assert detailed_info == expected_info
