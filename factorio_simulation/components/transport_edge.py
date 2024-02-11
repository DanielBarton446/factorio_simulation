from factorio_simulation.components.component import Component
from factorio_simulation.utils import get_logger

logger = get_logger(__name__)


class TransportEdge(Component):
    """
    This will contain the x,y coordinates of the source
    and destination locations of where an object is moving
    between
    """

    def __init__(self, source: (int, int), destination: (int, int)):
        super().__init__()
        self.source = source
        self.destination = destination
        logger.debug(f"Created Component ({self.component_id}) {self}")

    def __hash__(self):
        return hash(type(self))

    def __eq__(self, other):
        return self.source == other.source and self.destination == other.destination

    def __repr__(self):
        return f"TransportEdge({self.source}, {self.destination})"

    def to_dict(self):
        return {
            "TransportEdge": {"source": self.source, "destination": self.destination}
        }
