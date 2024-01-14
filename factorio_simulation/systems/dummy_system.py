from typing import Optional, List
from factorio_simulation.entities.entity import Entity
from factorio_simulation.systems.system import System
from factorio_simulation.components.dummy_component import DummyComponent


class DummySystem(System):
    def __init__(self, base_entities: Optional[List[Entity]] = None):
        self.entities = base_entities or []

    def update(self, current_tick):
        if current_tick % 60 != 0:
            return

        for entity in self.entities:
            if entity.has_component_type(DummyComponent):
                print(f'Entity {entity.entity_id} has dummy component')
