from factorio_simulation.components.component import Component
from typing import Set, Optional


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

    def get_component(self, component_type: type) -> Optional[Component]:
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None

    def has_component_type(self, component_type: type) -> bool:
        for component in self.components:
            if type(component) is component_type:
                return True
            
        return False
