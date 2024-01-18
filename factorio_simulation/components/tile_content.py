from factorio_simulation.components.component import Component
from uuid import UUID


class TileContent(Component):

    def __init__(self, ent_id: UUID, content=''):
        self.manifested_entity_id = ent_id
        self.content = content
        super().__init__()

    def __hash__(self):
        return hash(type(self))

    def __eq__(self, other):
        if not isinstance(other, TileContent):
            return False
        return self.content == other.content

    def __str__(self):
        return str(self.content)
