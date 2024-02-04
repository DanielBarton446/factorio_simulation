from typing import Optional, List, Dict
from factorio_simulation.components.transport_edge import TransportEdge
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.components.position import Position
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.entity_registry import EntityRegistry
from factorio_simulation.entities.tile import Tile
from factorio_simulation.systems.system import System

from factorio_simulation.utils import get_logger

from numpy.typing import NDArray

logger = get_logger(__name__)

class InteractionMovementSystem(System):
    """
    This system is responsible for the interactions of
    entities which move other entities on the map.
    """

    def __init__(self,
                 entity_registry: EntityRegistry,
                 world: NDArray[Tile],
                 base_entities: Optional[Dict[type, List[Entity]]] = None):

        super().__init__(entity_registry=entity_registry,
                         base_entities=base_entities)

        self.world = world

    def update(self, current_tick):
        if current_tick % 100 == 0:
            for entity_list in self.entities.values():
                for entity in entity_list:
                    if self.remove_entity_if_deleted(entity):
                        continue

                    source: (int, int) = entity.get_component(TransportEdge).source
                    dest: (int, int) = entity.get_component(TransportEdge).destination

                    if self.world[source[1]][source[0]].get_component(TileContent).content == '.':
                        # skip as we have nothing to move from source to dest
                        continue

                    if self.world[dest[1]][dest[0]].get_component(TileContent).content != '.':
                        # skip as we have something in the way
                        continue

                    source_tile_entity = self.world[source[1]][source[0]]
                    source_tile_component = source_tile_entity.get_component(TileContent)

                    # update the entity that lives in the tile:
                    real_entity = self.entity_registry.get(source_tile_component.manifested_entity_id)
                    if real_entity is None:
                        raise Exception(f"Entity {source_tile_component.manifested_entity_id} not found in registry. This should be impossible")
                    real_entity.update_component(Position(dest[0], dest[1]))

                    source_tile_entity.update_component(TileContent(ent_id=None))
                    dest_tile_entity = self.world[dest[1]][dest[0]]
                    dest_tile_entity.update_component(source_tile_component)
