from factorio_simulation.components.position import Position
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.entities.entity import Entity
from factorio_simulation.utils import get_logger

logger = get_logger(__name__)


class Inserter(Entity):

    def __init__(self, img: str, x, y):
        super().__init__()
        self.add_component(Position(x, y))
        self.add_component(TileContent(self.entity_id, img))

        logger.debug(f"Created Entity: ({self.entity_id}) {self}")

    def __str__(self):
        tile_content = self.get_component(TileContent)
        return f"{tile_content}"
