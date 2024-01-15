from typing import Optional, List
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.tile import Tile
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.components.position import Position
from factorio_simulation.systems.system import System

import numpy
from numpy.typing import ArrayLike


class WorldSystem(System):
    def __init__(self, base_entities: Optional[List[Entity]] = None,
                 width: int = 0, height: int = 0):
        super().__init__(base_entities)
        self.width = width
        self.height = height
        self.world: ArrayLike[Tile] = self.__empty_map(self.width, self.height)
        print("Base: " + str(len(base_entities)))

    def __empty_map(self, width, height):
        vec = numpy.empty(width * height, dtype=Tile)
        for i in range(width * height):
            tile = Tile(1337, i % width, i // width)
            vec[i] = tile
            self.add_entity(tile)
        dimensionalized_map = vec.reshape(width, height)
        return dimensionalized_map

    def render(self):
        for row in self.world:
            for tile in row:
                print(tile, end=' ')
            print()

    def update(self, current_tick):
        # silly, but we don't want a mess
        if current_tick % 100 == 0:
            print(current_tick)
            self.render()

        for (i, entity) in enumerate(self.entities):
            if entity.has_component_type(TileContent):
                if i % 3 == 0:
                    entity.remove_component(TileContent)
                    entity.add_component(TileContent(123, 'X'))
