from typing import Optional, List, Dict
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.dummy_entity import DummyEntity
from factorio_simulation.systems.system import System
from factorio_simulation.components.dummy_component import DummyComponent


class DummySystem(System):
    def __init__(self, base_entities: Optional[Dict[type, List[Entity]]] = None):
        super().__init__(base_entities)

    def update(self, current_tick):
        if current_tick % 60 != 0:
            return

        for entity in self.entities[DummyEntity]:
            if entity.has_component_type(DummyComponent):
                name = entity.get_component(DummyComponent).name
                print(f"Entity {entity.entity_id}: Hello, my name is {name}!")
            else:
                print(
                    f"{type(entity)}: does not have component of type: {DummyComponent}"
                )
