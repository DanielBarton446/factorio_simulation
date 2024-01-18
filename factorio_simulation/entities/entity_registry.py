from factorio_simulation.entities.entity import Entity

from uuid import UUID
from typing import Dict


class EntityRegistry:
    """A registry of entities."""

    def __init__(self):
        """Initialize the registry."""
        self._entities: Dict[UUID, Entity] = {}

    def register(self, entity: Entity):
        """Register an entity."""
        self._entities[entity.entity_id] = entity

    def unregister(self, entity: Entity):
        """Unregister an entity."""
        del self._entities[entity.entity_id]

    def unregister_by_id(self, entity_id: UUID):
        """Unregister an entity."""
        del self._entities[entity_id]

    def get(self, entity_id: UUID):
        """Get an entity by its id."""
        return self._entities.get(entity_id)

    def get_all(self):
        """Get all entities."""
        return self._entities.values()

    def __iter__(self):
        """Iterate over the entities."""
        return iter(self._entities.values())
