from typing import Optional, List
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.tile import Tile
from factorio_simulation.entities.fire import Fire
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
            new_fire = Fire()
            self.add_entity(new_fire)
            tile_to_corrupt = random.choice(self.entities[Tile])
            tile_to_corrupt.update_component(
                new_fire.get_component(TileContent))
