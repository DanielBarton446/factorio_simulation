from enum import Enum

from factorio_simulation.components.position import Position
from factorio_simulation.components.rotation import Rotation
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.components.transport_edge import TransportEdge
from factorio_simulation.entities.ab_entity_factory import \
    AbstractEntityFactory
from factorio_simulation.entities.entity import Entity
from factorio_simulation.entities.inserter import Inserter


class Orientation(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class InserterFactory(AbstractEntityFactory):
    def create_entity(self, orientation: Orientation, x: int, y: int) -> Entity:

        transport = None
        img = ""
        if orientation == Orientation.UP:
            transport = TransportEdge((x, y + 1), (x, y - 1))
            img = "↑"
        elif orientation == Orientation.DOWN:
            transport = TransportEdge((x, y - 1), (x, y + 1))
            img = "↓"
        elif orientation == Orientation.LEFT:
            transport = TransportEdge((x + 1, y), (x - 1, y))
            img = "←"
        elif orientation == Orientation.RIGHT:
            transport = TransportEdge((x - 1, y), (x + 1, y))
            img = "→"
        else:
            raise ValueError(f"Invalid orientation: {orientation}")

        inserter = Inserter(img, x, y)
        inserter.add_component(Rotation(72))
        inserter.add_component(transport)

        return inserter
