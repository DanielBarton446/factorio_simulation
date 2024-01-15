from factorio_simulation.components.component import Component
import randomname


class DummyComponent(Component):
    def __init__(self, component_id):
        super().__init__(component_id)
        self.name = randomname.generate('names/surnames/english')
