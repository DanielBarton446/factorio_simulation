from factorio_simulation.components.component import Component
from factorio_simulation.utils import get_logger


logger = get_logger(__name__)


class Position(Component):
    """
        This position will have (x,y) coordinates,
        truthful to x position and y position.

        It is up to the user to adjust for any
        issues with how x and y are represented in arrays.
    """

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        logger.debug(f"Created Component ({self.component_id}) {self}")

    def __hash__(self):
        return hash(type(self))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def to_dict(self):
        return {
            "Position": {
                "x": self.x,
                "y": self.y
            }
        }
