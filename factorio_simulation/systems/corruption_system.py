from typing import Optional, List
from factorio_simulation.entities.entity import Entity
from factorio_simulation.systems.system import System
from factorio_simulation.components.tile_content import TileContent

import random


class CorruptionSystem(System):
    def __init__(self,
                 base_entities: List[Entity] = None,
                 tick_rate: Optional[int] = 750):

        self.tick_rate = tick_rate
        super().__init__(base_entities)

    def update(self, current_tick):
        if current_tick % self.tick_rate == 0:
            to_corrupt = random.choice(self.entities)
            to_corrupt.update_component(TileContent(666, '󰈸'))
