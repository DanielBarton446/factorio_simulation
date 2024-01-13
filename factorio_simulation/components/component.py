

class Component:

    def __init__(self, component_id):
        self.entity_id = component_id

    def __hash__(self):
        return hash(type(self))

    def update(self, current_tick):
        pass
