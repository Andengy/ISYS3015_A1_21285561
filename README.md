# Pet Adoption System

## Project Description

The Pet Adoption System is a command-line application designed to manage pet information in a shelter. It allows users to perform various actions such as listing all pets, adding new pets, searching for pets by type, breed, or age, adopting pets, and displaying detailed information about each pet. The system supports saving and loading data from a CSV file to persist information between sessions.

## Features

- **List All Pets:** View details of all pets currently in the shelter.
- **Add a New Pet:** Add a new pet to the shelter with information such as ID, name, breed, age, and description.
- **Search for a Pet:** Search for pets by type, breed, or age.
- **Adopt a Pet:** Mark a pet as adopted.
- **Display Pet Details:** View detailed information about a specific pet.
- **Save Shelter Data:** Save the current state of the shelter to a CSV file.
- **Load Shelter Data:** Load pet data from a CSV file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pet-adoption-system.git
    cd pet-adoption-system
    ```

2. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. Follow the on-screen prompts to interact with the system.

## Running Tests

1. Ensure the virtual environment is activated.
2. Run the tests using pytest:
    ```sh
    pytest
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
