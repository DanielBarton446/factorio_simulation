from typing import Optional, List
from factorio_simulation.entities.tile import Tile
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.components.position import Position
from factorio_simulation.systems.system import System
from numpy.typing import ArrayLike

import numpy


class WorldSystem(System):
    def __init__(self, width: int = 0, height: int = 0,
                 base_entities: Optional[List[Tile]] = None):
        super().__init__(base_entities)
        self.width = width
        self.height = height
        self.world: ArrayLike = self.__empty_map(width, height)

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

    def __empty_map(self, width, height) -> ArrayLike:
        vec = numpy.empty(width * height, dtype=Tile)
        for i in range(width * height):
            tile = Tile(1337, i % width, i // width, content='')
            vec[i] = tile
            self.add_entity(tile)
        dimensionalized_map = vec.reshape(width, height)
        return dimensionalized_map

    def update(self, current_tick):
        # Iterate through the world and update the position of each tile
        # if they have been moved from their original position.

        for (y, vals) in enumerate(self.world):
            for x, tile in enumerate(vals):
                comp_pos = tile.get_component(Position)
                if self.world[comp_pos.y][comp_pos.x] != tile:
                    evicted = self.get_tile(x, y)
                    evicted.update_component(TileContent(-42))
                    self.set_tile(evicted, x, y)
                    self.set_tile(tile, comp_pos.x, comp_pos.y)
                position = tile.get_component(Position)
                self.world[position.y][position.x] = tile
