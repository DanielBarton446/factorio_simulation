from factorio_simulation.components.component import Component


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

    def __hash__(self):
        return hash(type(self))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
