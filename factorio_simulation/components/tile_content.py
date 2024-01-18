from factorio_simulation.components.component import Component
from uuid import UUID
from factorio_simulation.utils import get_logger


logger = get_logger(__name__)


class TileContent(Component):

    def __init__(self, ent_id: UUID, content=''):
        super().__init__()
        self.manifested_entity_id = ent_id
        self.content = content
        logger.debug(f"Created Component ({self.component_id}) {self}")


    def __hash__(self):
        return hash(type(self))

    def __eq__(self, other):
        if not isinstance(other, TileContent):
            return False
        return self.content == other.content


    def __repr__(self):
        return f"TileContent({self.content})"

    def __str__(self):
        return str(self.content)
