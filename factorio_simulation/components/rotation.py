from factorio_simulation.components.component import Component
from factorio_simulation.utils import get_logger


logger = get_logger(__name__)


class Rotation(Component):
    """
    After N ticks, the object will have rotated 360 degrees, or
    1 full 'turn'.

    self.current_rotation_tick is a way to keep track of how
    many ticks have passed since the last rotation.
    """

    def __init__(self, ticks_per_full_turn: int):
        super().__init__()
        self.ticks_per_full_turn = ticks_per_full_turn
        self.current_tick = 0
        logger.debug(f"Created Component ({self.component_id}) {self}")

    def __hash__(self):
        return hash(type(self))

    def __eq__(self, other):
        return self.ticks_per_full_turn == other.ticks_per_full_turn

    def __repr__(self):
        return f"Rotation({self.ticks_per_full_turn})"

    def to_dict(self):
        return {"Rotation": {"rotation": self.ticks_per_full_turn}}
