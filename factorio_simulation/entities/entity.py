from factorio_simulation.components.component import Component
from typing import Set


class Entity:

    def __init__(self, entity_id):
        self.entity_id: int = entity_id
        self.components: Set[Component] = set()

    def add_component(self, component: Component):
        # we will make it so that Component has a hash 
        # function that returns the component type
        self.components.add(component)

    # def remove_component(self, component_type: type):
    #     self.components.remove(component_type)

    def get_component(self, component_type: type):
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None

    def update(self, current_tick):
        for component in self.components:
            component.update(current_tick)
