from factorio_simulation.components.component import Component

class DummyComponent(Component):
    def __init__(self, component_id):
        super().__init__(component_id)
        self.name = "DummyComponent"

    def update(self, current_tick):
        if current_tick % 60 == 0:
            print("DummyComponent.update() called")
