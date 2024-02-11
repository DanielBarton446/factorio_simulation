from abc import ABC, abstractmethod

from factorio_simulation.entities.entity import Entity


class AbstractEntityFactory(ABC):
    @abstractmethod
    def create_entity(self) -> Entity:
        pass
