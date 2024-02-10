from typing import Optional, List
from factorio_simulation.entities.tile import Tile
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.entity_registry import EntityRegistry
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.components.position import Position
from factorio_simulation.systems.system import System
from numpy.typing import NDArray

from factorio_simulation.utils import get_logger

import numpy

logger = get_logger(__name__)


class WorldSystem(System):
    def __init__(
        self,
        entity_registry: EntityRegistry,
        width: int = 0,
        height: int = 0,
        base_entities: Optional[List[Tile]] = None,
    ):
        super().__init__(entity_registry, base_entities)
        self.width = width
        self.height = height
        self.__world: NDArray[Tile] = self.__empty_map(width, height)

    def get_readable_world(self):
        return self.__world.view()

    def place_entity(self, entity: Entity) -> None:
        # really wish we had a where clause here
        # to ensure Entity has the components we need
        # so we would get compile time errors.

        if not entity.has_component_type(Position) or not entity.has_component_type(
            TileContent
        ):
            logger.error("Entity does not have the required components")
            return

        position = entity.get_component(Position)
        tile_content = entity.get_component(TileContent)
        self.set_tile_content(tile_content, position.x, position.y)
        return

    def get_tile(self, x: int, y: int) -> Tile:
        """
        Gets the tile at the given coordinates.
        Primarily used for consistency in world access.

        @param x: the cartesian x coordinate of the tile
        @param y: the cartesian y coordinate of the tile
        @retuns the tile at the given coordinates.
        """
        return self.__world[y][x]

    def set_tile(self, tile: Tile, x: int, y: int):
        """
        Sets the tile at the given coordinates to the given tile.
        Primarily used for consistency in world access.

        @param x: the cartesian x coordinate of the tile
        @param y: the cartesian y coordinate of the tile
        @param tile: the tile to set at the given coordinates.
        """
        self.__world[y][x] = tile

    def set_tile_content(self, content: TileContent, x: int, y: int):
        """
        Sets the tile content at the given coordinates to the given content.
        Primarily used for consistency in world access.

        @param x: the cartesian x coordinate of the tile
        @param y: the cartesian y coordinate of the tile
        @param content: the content to set at the given coordinates.
        """

        self.__world[y][x].update_component(content)

    def __empty_map(self, width, height) -> NDArray[Tile]:
        vec = numpy.empty(width * height, dtype=Tile)
        for i in range(width * height):
            tile = Tile(i % width, i // width)
            vec[i] = tile
            self.add_entity(tile)
        dimensionalized_map = vec.reshape(width, height)
        return dimensionalized_map

    def update(self, current_tick):
        # Iterate through the world and update the position of each tile
        # if they have been moved from their original position.

        for y, vals in enumerate(self.__world):
            for x, tile in enumerate(vals):
                comp_pos = tile.get_component(Position)
                if self.__world[comp_pos.y][comp_pos.x] != tile:
                    evicted = self.get_tile(x, y)
                    evicted.update_component(TileContent(ent_id=None))
                    self.set_tile(evicted, x, y)
                    self.set_tile(tile, comp_pos.x, comp_pos.y)
                position = tile.get_component(Position)
                self.__world[position.y][position.x] = tile
