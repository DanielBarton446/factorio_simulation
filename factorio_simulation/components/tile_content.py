from factorio_simulation.components.component import Component


class TileContent(Component):

    def __init__(self, component_id, content=''):
        self.content = content
        super().__init__(component_id)

    def __hash__(self):
        return hash(type(self))

    def __eq__(self, other):
        if not isinstance(other, TileContent):
            return False
        return self.content == other.content

    def __str__(self):
        return str(self.content)
