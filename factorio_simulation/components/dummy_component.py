import randomname

from factorio_simulation.components.component import Component


class DummyComponent(Component):
    def __init__(self):
        super().__init__()
        self.name = randomname.generate("names/surnames/english")
