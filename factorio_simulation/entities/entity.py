from factorio_simulation.components.component import Component
from typing import Dict, Optional


class Entity:
    """
    An entity is a collection of components.
    """

    def __init__(self, entity_id):
        """
        @param entity_id: The unique id of the entity
        @param components: Set of components that the entity has
        """

        self.entity_id: int = entity_id
        self.components: Dict = dict()

    def add_component(self, component: Component):
        """
        Add a component to the entity
        """
        if self.components.get(type(component)) is not None:
            raise Exception("Entity already has a component of type: ",
                            type(component))
        self.components[type(component)] = component

    def remove_component(self, component_type: type):
        del self.components[component_type]

    def get_component(self, component_type: type) -> Optional[Component]:
        """
        Given the type of component, return the component on the entity.
        """
        return self.components.get(component_type)

    def has_component_type(self, component_type: type) -> bool:
        """
        Given the type of component, return True if the entity
        has the component.
        """

        return self.components.get(component_type) is not None

