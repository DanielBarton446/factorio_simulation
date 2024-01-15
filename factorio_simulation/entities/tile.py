from factorio_simulation.entities.entity import Entity
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.components.position import Position


class Tile(Entity):

    def __init__(self, id, x, y, content=None):
        super().__init__(id)

        self.add_component(TileContent(420, content))
        self.add_component(Position(420, x, y))

    def __repr__(self):
        tile_content = self.get_component(TileContent)
        return f'{tile_content}'

    def __str__(self):
        tile_content = self.get_component(TileContent)
        return f'{tile_content}'
