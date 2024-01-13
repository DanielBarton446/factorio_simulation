from typing import Optional, List
from factorio_simulation.entities.entity import Entity
from factorio_simulation.systems.system import System


class WorldSystem(System):
    def __init__(self, base_entities: Optional[List[Entity]] = None):
        self.entities = base_entities or []
