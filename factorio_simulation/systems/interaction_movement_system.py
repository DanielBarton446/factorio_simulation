from typing import Optional, List, Dict
from factorio_simulation.components.transport_edge import TransportEdge
from factorio_simulation.components.rotation import Rotation
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

    Should likely be used strictly for rotation movement entities.
    """

    def __init__(
        self,
        entity_registry: EntityRegistry,
        world: NDArray[Tile],
        base_entities: Optional[Dict[type, List[Entity]]] = None,
    ):

        super().__init__(entity_registry=entity_registry, base_entities=base_entities)

        self.world = world

    def increment_rotation_tick(self, entity: Entity):
        if not entity.has_component_type(Rotation):
            raise Exception(
                f"Entity {entity} is missing a Rotation component. This should be impossible"
            )
        rotation: Rotation = entity.get_component(Rotation)

        # this seems wrong for having the inserter go back and fourth
        rotation.current_tick += 1
        if rotation.current_tick >= rotation.ticks_per_full_turn:
            rotation.current_tick = 0

    def update(self, current_tick):
        for entity_list in self.entities.values():
            for entity in entity_list:
                if self.remove_entity_if_deleted(entity):
                    continue

                if not entity.has_component_type(TransportEdge):
                    raise Exception(
                        f"Entity {entity} is missing a TransportEdge component. This should be impossible"
                    )
                if not entity.has_component_type(Rotation):
                    raise Exception(
                        f"Entity {entity} is missing a Rotation component. This should be impossible"
                    )

                source: (int, int) = entity.get_component(TransportEdge).source
                dest: (int, int) = entity.get_component(TransportEdge).destination

                if (
                    self.world[source[1]][source[0]].get_component(TileContent).content
                    == "."
                ):
                    # skip as we have nothing to move from source to dest
                    continue

                if (
                    self.world[dest[1]][dest[0]].get_component(TileContent).content
                    != "."
                ):
                    # skip as we have something in the way
                    continue

                # now we are in a state where there is an item at
                # A -> B and B is empty. We can move the item

                self.increment_rotation_tick(entity)
                rotation = entity.get_component(Rotation)
                half_turn = rotation.ticks_per_full_turn // 2
                logger.debug(f"ROTATION: {rotation.current_tick}")
                logger.debug(f"Half Turn: {half_turn}")
                if rotation.current_tick % half_turn != 0:
                    logger.debug(f"Rotating: {rotation.current_tick}")
                    continue

                # should extract this out a bit more.
                source_tile_entity = self.world[source[1]][source[0]]
                source_tile_component = source_tile_entity.get_component(TileContent)

                # update the entity that lives in the tile:
                real_entity = self.entity_registry.get(
                    source_tile_component.manifested_entity_id
                )
                if real_entity is None:
                    raise Exception(
                        f"Entity {source_tile_component.manifested_entity_id} not found in registry. This should be impossible"
                    )
                real_entity.update_component(Position(dest[0], dest[1]))

                source_tile_entity.update_component(TileContent(ent_id=None))
                dest_tile_entity = self.world[dest[1]][dest[0]]
                dest_tile_entity.update_component(source_tile_component)
