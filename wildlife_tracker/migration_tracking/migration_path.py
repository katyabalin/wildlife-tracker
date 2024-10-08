from typing import Optional, Any
from wildlife_tracker.habitat_management.habitat import Habitat  


class MigrationPath:
    def __init__(self, path_id: int, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        self.path_id = path_id
        self.start_location = start_location
        self.destination = destination
        self.duration = duration or 0

    def get_path_details(self) -> dict[str, Any]:
        return {
            'path_id': self.path_id,
            'start_location': self.start_location.get_habitat_details(),
            'destination': self.destination.get_habitat_details(),
            'duration': self.duration  # Include the duration in path details
        }

    def update_path_details(self, **kwargs: dict[str, Any]) -> None:
        # Updates path details dynamically based on kwargs
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)