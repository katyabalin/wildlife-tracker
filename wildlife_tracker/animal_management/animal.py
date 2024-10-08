from typing import Any, Optional

class Animal:
    def __init__(self, animal_id: int, age: Optional[int] = None, species: str = "Unknown", health_status: Optional[str] = None):
        self.animal_id = animal_id
        self.age = age
        self.species = species
        self.health_status = health_status

    def update_animal_details(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

