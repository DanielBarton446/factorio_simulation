from typing import Optional, List
from factorio_simulation.configs.config import load_config
from factorio_simulation.systems.dummy_system import DummySystem
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.dummy_entity import DummyEntity
from factorio_simulation.components.dummy_component import DummyComponent

class DummySimulation:
    def __init__(self, config_file_name: Optional[str] = None):
        self.config = self._load_config(config_file_name)

        initial_entities: List[Entity] = self._arbitrary_entities()

        self.dummy_system = DummySystem(initial_entities)
        self.current_tick = 0

    def _load_config(self, config_file_name: Optional[str]):
        if config_file_name is None:
            return load_config()
        else:
            return load_config(config_file_name)

    def _arbitrary_entities(self):
        entities: List[Entity] = []
        for i in range(10):
            entities.append(DummyEntity(i))

        for j in range(5):
            comp = DummyComponent(j)
            entities[j].add_component(comp)

        return entities

    def run(self):
        while self.current_tick < self.config.runtime_ticks:
            self.current_tick += 1
            print(f'Running tick {self.current_tick}')
            self.dummy_system.update(self.current_tick)