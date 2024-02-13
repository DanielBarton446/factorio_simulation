import json
from typing import Optional

from factorio_simulation.components.position import Position
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.configs.config import load_config
from factorio_simulation.entities.berries import Berries
from factorio_simulation.entities.entity_registry import EntityRegistry
from factorio_simulation.entities.inserter import Inserter
from factorio_simulation.entities.inserter_factory import InserterFactory, Orientation
from factorio_simulation.systems.corruption_system import CorruptionSystem
from factorio_simulation.systems.interaction_movement_system import (
    InteractionMovementSystem,
)
from factorio_simulation.systems.renderer import Renderer
from factorio_simulation.systems.system_manager import SystemManager
from factorio_simulation.systems.world_system import WorldSystem
from factorio_simulation.utils import get_logger

logger = get_logger(__name__)


class WorldSimulation:

    def __init__(
        self, should_render: bool = True, config_file_name: Optional[str] = None
    ):
        self.config = self._load_config(config_file_name)
        self.current_tick = 0

        self.entity_registry = EntityRegistry()
        self.system_manager = SystemManager()
        world = WorldSystem(
            entity_registry=self.entity_registry,
            width=self.config.width,
            height=self.config.height,
        )
        self.system_manager.append(world)
        self.system_manager.append(
            InteractionMovementSystem(
                entity_registry=self.entity_registry,
                world=world.get_readable_world(),
            )
        )

        self.inserter_factory: InserterFactory = InserterFactory()
        self.add_inserter(2, 1, Orientation.RIGHT)
        self.add_inserter(3, 2, Orientation.DOWN)
        self.add_inserter(2, 3, Orientation.LEFT)
        self.add_inserter(1, 2, Orientation.UP)

        self.add_inserter(0, 0, Orientation.RIGHT)
        self.add_inserter(1, 0, Orientation.RIGHT)

        self.system_manager.append(
            CorruptionSystem(
                entity_registry=self.entity_registry,
                base_entities=world.entities,
                tick_rate=200,
            )
        )
        self.system_manager.set_renderer(
            Renderer(
                world=world.get_readable_world(),
                tick_rate=1,
            )
        )
        if should_render:
            self.system_manager.set_renderer(
                Renderer(world=world.get_readable_world(), tick_rate=1)
            )

        super().__init__()

    def add_inserter(self, x: int, y: int, orientation: Orientation):
        inserter = self.inserter_factory.create_entity(orientation, x, y)
        world_system: WorldSystem = self.system_manager.get_system(WorldSystem)
        interaction_system: InteractionMovementSystem = self.system_manager.get_system(
            InteractionMovementSystem
        )
        world_system.place_entity(inserter)
        interaction_system.add_entity(inserter)
        self.entity_registry.register(inserter)

    def _load_config(self, config_file_name: Optional[str]):
        if config_file_name is None:
            return load_config()
        else:
            return load_config(config_file_name)

    def sim_json(self):
        state = [sys.to_dict() for sys in self.system_manager.systemc]
        return json.dumps(state)

    def run(self):
        try:
            while self.current_tick <= self.config.runtime_ticks:
                logger.debug(f"Tick: {self.current_tick}")
                if self.current_tick == 50:
                    berries = Berries(x=1, y=1)
                    self.entity_registry.register(berries)
                    world = self.system_manager.get_system(WorldSystem)
                    world.place_entity(berries)

                for system in self.system_manager.all_system():
                    system.update(self.current_tick)
                self.current_tick += 1
        except Exception as e:
            # is there a better way to do this?
            logger.exception(e)
            renderer = self.system_manager.renderer
            if renderer:
                renderer.teardown()
            raise e
