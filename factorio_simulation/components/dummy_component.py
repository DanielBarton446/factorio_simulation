from factorio_simulation.components.component import Component

class DummyComponent(Component):
    def __init__(self, component_id):
        super().__init__(component_id)
        self.name = "DummyComponent"
