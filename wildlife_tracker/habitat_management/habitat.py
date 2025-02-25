from typing import Any, List, Optional
from wildlife_tracker.animal_management.animal import Animal



class Habitat:

    def __init__(self,
                habitat_id: int,
                geographic_area: str,
                size: int,
                environment_type: str,
                animals: Optional[List[Animal]] = None) -> None:
        self.habitat_id = habitat_id
        self.geographic_area = geographic_area
        self.size = size
        self.environment_type = environment_type
        # this is Pythonic for
        # if animals is not None:
        #   self.animals = animals
        # else:
        #   self.animals = []
        self.animals = animals or []

    def update_habitat_details(self, **kwargs: dict[str: Any]) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self,key, value)
 

    def assign_animals_to_habitat(self, animals: List[Animal]) -> None:
        self.animals.extend(animals)
    

    def get_animals_in_habitat(self) -> List[Animal]:
        return self.animals
    

    def get_habitat_details(self) -> dict:
        return {
            'habitat_id': self.habitat_id,
            'geographic_area': self.geographic_area,
            'size': self.size,
            'environment_type': self.environment_type,
            'animals': [animal.animal_id for animal in self.animals] 
    }
    