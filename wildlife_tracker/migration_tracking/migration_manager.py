from typing import Optional, Dict
from wildlife_tracker.migration_tracking.migration_path import MigrationPath



class MigrationManager:
    def __init__(self) -> None:
        self.migration_paths: Dict[int, MigrationPath] = {}

    def register_migration_path(self, migration_path: MigrationPath) -> None:
        self.migration_paths[migration_path.path_id] = migration_path

    def get_migration_path_by_id(self, path_id: int) -> Optional[MigrationPath]:
        return self.migration_paths.get(path_id)

    def remove_migration_path(self, path_id: int) -> None:
        if path_id in self.migration_paths:
            del self.migration_paths[path_id]

    def schedule_migration(self, migration_path: MigrationPath) -> None:
        print(f"Migration from {migration_path.start_location.habitat_id} to {migration_path.destination.habitat_id} has been scheduled.")