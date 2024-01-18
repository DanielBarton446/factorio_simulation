from typing import Optional, List, Dict
from factorio_simulation.components.transport_edge import TransportEdge
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.entity_registry import EntityRegistry
from factorio_simulation.entities.tile import Tile
from factorio_simulation.systems.system import System

from numpy.typing import NDArray


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
        # eventually we will use the ticks of the
        # entity to determine if we update the map or not
        if current_tick % 100 == 0:
            for entity_list in self.entities.values():
                for entity in entity_list:
                    # this should be handled better (x, y) should ideally be
                    # used with a functinon call so we don't have to think 
                    # about the order of dimensions
                    source: (int, int) = entity.get_component(TransportEdge).source
                    dest: (int, int) = entity.get_component(TransportEdge).destination

                    source_entity = self.world[source[1]][source[0]]
                    source_component = source_entity.get_component(TileContent)
                    source_entity.update_component(TileContent(None))

                    dest_entity = self.world[dest[1]][dest[0]]
                    # should at some point make sure nothing is here that we are overwriting
                    # dest_component = dest_entity.get_component(TileContent)
                    dest_entity.update_component(source_component)
