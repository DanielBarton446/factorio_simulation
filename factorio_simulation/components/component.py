

class Component:

    def __init__(self, component_id):
        self.component_id = component_id

    def __hash__(self):
        return hash(type(self))
