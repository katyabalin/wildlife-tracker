from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.habitat_management.habitat_manager import HabitatManager
from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.animal_management.animal_manager import AnimalManager

# Create a Habitat and AnimalManager
habitat_manager = HabitatManager()
animal_manager = AnimalManager()

# Register an Animal
animal = Animal(animal_id=1, age=5, species="Lion")
animal_manager.register_animal(animal)

# Create a Habitat
habitat = Habitat(habitat_id=101, geographic_area="Savannah", size=1000, environment_type="Grassland")
habitat_manager.register_habitat(habitat)

# Assign animals to habitat
habitat.assign_animals_to_habitat([animal])

# Check habitat details
print(habitat.get_habitat_details())

# Retrieve habitat by ID
retrieved_habitat = habitat_manager.get_habitat_by_id(101)
print(retrieved_habitat.get_habitat_details())

# Remove habitat
habitat_manager.remove_habitat(101)


