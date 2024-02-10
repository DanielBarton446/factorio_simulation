from factorio_simulation.components.component import Component
from typing import Dict, Optional
from uuid import uuid4
from uuid import UUID

from factorio_simulation.utils import get_logger

logger = get_logger(__name__)


class Entity:
    """
    An entity is a collection of components.
    """

    def __init__(self):
        """
        @param entity_id: The unique id of the entity
        @param components: Set of components that the entity has
        """

        self.entity_id: UUID = uuid4()
        self.components: Dict = dict()

    def update_component(self, component: Component):
        """
        NOTE: this is more performant than add_component, but at
        the cost of overwriting the component if it already exists.

        Set or update a component on the entity if it already exists.
        """
        self.components[type(component)] = component

    def add_component(self, component: Component):
        """
        Add a component to the entity
        """
        if self.components.get(type(component)) is not None:
            raise Exception("Entity already has a component of type: ", type(component))
        self.components[type(component)] = component

    def remove_component(self, component_type: type):
        """
        Given the type of component, remove it from this entity
        """
        del self.components[component_type]

    def get_component(self, component_type: type) -> Optional[Component]:
        """
        Given the type of component, return the component on the entity.
        """
        try:
            return self.components[component_type]
        except KeyError:
            logger.exception(
                f"{self.entity_id} does not have a component of type: {component_type}"
            )
            raise Exception(
                f"{self.entity_id} does not have a component of type: {component_type}"
            )

    def has_component_type(self, component_type: type) -> bool:
        """
        Given the type of component, return True if the entity
        has the component.
        """

        return self.components.get(component_type) is not None

    def to_dict(self) -> Dict:
        """
        Return a dictionary representation of the entity
        """
        # we know that there can only be 1 type of each component, so
        # we make an object instead of a list
        return {
            self.__class__.__name__: {
                "entity_id": str(self.entity_id),
                "components": [
                    component.to_dict() for component in self.components.values()
                ],
            }
        }

    def __repr__(self):
        pass

    def __str__(self):
        pass
