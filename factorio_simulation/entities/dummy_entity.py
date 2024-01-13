from factorio_simulation.entities.entity import Entity

class DummyEntity(Entity):
    def __init__(self, id):
        super().__init__(id)

    def update(self, current_tick):
        print("DummyEntity.update() called")
        super().update(current_tick)
