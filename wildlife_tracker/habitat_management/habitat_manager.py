from typing import Optional, Dict, List
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.animal_management.animal import Animal

class HabitatManager:

    def __init__(self) -> None:
       
        self.habitats: Dict[int, Habitat] = {}

    def register_habitat(self, habitat: Habitat) -> None:
        self.habitats[habitat.habitat_id] = habitat

    def get_habitat_by_id(self, habitat_id: int) -> Optional[Habitat]:
        return self.habitats.get(habitat_id)

    def remove_habitat(self, habitat_id: int) -> None:
        if habitat_id in self.habitats:
            del self.habitats[habitat_id]

    def assign_animals_to_habitat(self, habitat_id: int, animals: List[Animal]) -> None:
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            habitat.assign_animals_to_habitat(animals)
