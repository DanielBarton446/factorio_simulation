from factorio_simulation.components.component import Component
from factorio_simulation.utils import get_logger

logger = get_logger(__name__)


class Movable(Component):

    def __init__(self):
        super().__init__()
        logger.debug(f"Created Component ({self.component_id}) {self}")

    def __hash__(self):
        return hash(type(self))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def to_dict(self):
        return {"Movable": True}
