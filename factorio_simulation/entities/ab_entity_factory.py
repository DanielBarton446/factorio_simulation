from factorio_simulation.entities.entity import Entity
from abc import ABC, abstractmethod


class AbstractEntityFactory(ABC):
    @abstractmethod
    def create_entity(self) -> Entity:
        pass
