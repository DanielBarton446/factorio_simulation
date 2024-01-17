from factorio_simulation.entities.entity import Entity
from typing import List, Dict

from uuid import UUID


class System:

    def __init__(self, base_entities: Dict[type, List[Entity]] = None):
        self.entities: Dict[type, List[Entity]] = base_entities or dict()

    def add_entity(self, entity: Entity):
        if type(entity) not in self.entities:
            self.entities[type(entity)] = [entity]
        else:
            self.entities.get(type(entity)).append(entity)

    def remove_entity(self, entity: Entity):
        if type(entity) in self.entities:
            self.entities.get(type(entity)).remove(entity)

    def remove_entity_by_id(self, id: UUID) -> bool:
        for ent_type, entity_list in self.entities.items():
            for entity in entity_list:
                if entity.entity_id == id:
                    entity_list.remove(entity)
                    return True
        return False

    def update(self, current_tick):
        pass
