from collections import OrderedDict
from typing import List, Optional

from factorio_simulation.systems.renderer import Renderer
from factorio_simulation.systems.system import System


class SystemManager:
    def __init__(
        self,
        system_list: Optional[List[System]] = [],
        renderer: Optional[Renderer] = None,
    ):
        self.systems: Dict[type, System] = OrderedDict()
        for system in system_list:
            self.systems[system.__class__.__name__] = system
        self.renderer = renderer

    def all_system(self) -> List[System]:
        systems: List[System] = list(self.systems.values())
        if self.renderer:
            systems.append(self.renderer)
        return systems

    def update(self, dt):
        for system in self.systems:
            system.update(dt)

        if self.renderer:  # would be nice to not need this check.
            self.renderer.render()

    def set_renderer(self, renderer):
        self.renderer = renderer

    def append(self, system: System):
        self.systems[system.__class__.__name__] = system

    def get_system(self, system_type: type) -> System:
        return self.systems[system_type.__name__]
