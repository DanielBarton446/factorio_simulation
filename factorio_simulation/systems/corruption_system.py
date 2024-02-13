import random
from typing import List, Optional

from factorio_simulation.components.position import Position
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.entity_registry import EntityRegistry
from factorio_simulation.entities.fire import Fire
from factorio_simulation.entities.tile import Tile
from factorio_simulation.systems.system import System
from factorio_simulation.utils import get_logger

logger = get_logger(__name__)


class CorruptionSystem(System):
    def __init__(
        self,
        entity_registry: EntityRegistry,
        base_entities: List[Entity] = None,
        tick_rate: Optional[int] = 750,
    ):

        self.tick_rate = tick_rate
        super().__init__(entity_registry, base_entities)

    def get_tile_by_coordinates(self, pos: Position) -> Optional[Tile]:
        for tile in self.entities[Tile]:
            tile_pos = tile.get_component(Position)
            if tile_pos.x == pos.x and tile_pos.y == pos.y:
                return tile
        return None

    def update(self, current_tick):
        if current_tick % self.tick_rate == 0:
            entity_types_to_corrupt = list(self.entities.keys() - {Tile, Fire})

            if len(entity_types_to_corrupt) == 0:
                # no entity types to corrupt
                return

            corrupution_candidates = self.entities[
                random.choice(entity_types_to_corrupt)
            ]

            if len(corrupution_candidates) == 0:
                # no entities to corrupt
                return

            new_fire = Fire()
            self.add_entity(new_fire)

            corrupted_entity = random.choice(corrupution_candidates)
            self.entity_registry.unregister(corrupted_entity)
            # this seems kind of gross to have to do
            self.entities[type(corrupted_entity)].remove(corrupted_entity)

            tile_to_corrupt = self.get_tile_by_coordinates(
                corrupted_entity.get_component(Position)
            )
            if tile_to_corrupt is not None:
                tile_to_corrupt.update_component(new_fire.get_component(TileContent))
                logger.debug(
                    f"Corrupted ({corrupted_entity.entity_id}) at {corrupted_entity.get_component(Position)}"
                )
