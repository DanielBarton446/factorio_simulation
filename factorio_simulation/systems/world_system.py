from typing import Optional, List
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.tile import Tile
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.components.position import Position
from factorio_simulation.systems.system import System
from numpy.typing import ArrayLike

import numpy


class WorldSystem(System):
    def __init__(self, width: int = 0, height: int = 0,
                 base_entities: Optional[List[Entity]] = None):
        super().__init__(base_entities)
        self.width = width
        self.height = height
        self.world: ArrayLike[Tile] = self.__empty_map(width, height)

    def get_tile(self, x: int, y: int) -> Tile:
        """
        Gets the tile at the given coordinates.
        Primarily used for consistency in world access.

        @param x: the cartesian x coordinate of the tile
        @param y: the cartesian y coordinate of the tile
        @retuns the tile at the given coordinates.
        """
        return self.world[y][x]

    def set_tile(self, tile: Tile, x: int, y: int):
        """
        Sets the tile at the given coordinates to the given tile.
        Primarily used for consistency in world access.

        @param x: the cartesian x coordinate of the tile
        @param y: the cartesian y coordinate of the tile
        @param tile: the tile to set at the given coordinates.
        """
        self.world[y][x] = tile

    def __empty_map(self, width, height):
        vec = numpy.empty(width * height, dtype=Tile)
        for i in range(width * height):
            tile = Tile(1337, i % width, i // width, content='')
            vec[i] = tile
            self.add_entity(tile)
        dimensionalized_map = vec.reshape(width, height)
        return dimensionalized_map

    def render(self):
        for (y, vals) in enumerate(self.world):
            for x, tile in enumerate(vals):
                comp_pos = tile.get_component(Position)
                if self.world[comp_pos.y][comp_pos.x] != tile:
                    evicted = self.world[comp_pos.y][comp_pos.x]
                    evicted.update_component(TileContent(-42))
                    self.set_tile(tile, comp_pos.x, comp_pos.y)
                    self.set_tile(evicted, x, y)
                print(self.get_tile(x, y), end=' ')
            print()

    def update(self, current_tick):
        # Update position of entities in the world
        for entity in self.entities:
            if entity.has_component_type(Position):
                position = entity.get_component(Position)
                self.world[position.y][position.x] = entity

        print(f'{current_tick}')
        self.render()
