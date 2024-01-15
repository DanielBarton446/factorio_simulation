from factorio_simulation.entities.entity import Entity
from typing import List


class System:

    def __init__(self, base_entities: List[Entity] = None):
        self.entities: List[Entity] = base_entities or []

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def remove_entity(self, entity: Entity):
        self.entities.remove(entity)

    def remove_entity_by_id(self, id: int) -> bool:
        for entity in self.entities:
            if entity.entity_id == id:
                self.entities.remove(entity)
                return True
        return False

    def update(self, current_tick):
        pass
