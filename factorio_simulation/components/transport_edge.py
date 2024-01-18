from factorio_simulation.components.component import Component


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

    def __hash__(self):
        return hash(type(self))

    def __eq__(self, other):
        return self.source == other.source and \
               self.destination == other.destination
