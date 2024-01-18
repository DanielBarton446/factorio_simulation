from factorio_simulation.configs.config import load_config
from factorio_simulation.entities.entity_registry import EntityRegistry
from factorio_simulation.systems.world_system import WorldSystem
from factorio_simulation.systems.corruption_system import CorruptionSystem
from factorio_simulation.systems.renderer import Renderer
from typing import Optional


class WorldSimulation:

    def __init__(self, should_render: bool = True,
                 config_file_name: Optional[str] = None):
        self.config = self._load_config(config_file_name)
        self.current_tick = 0

        self.entity_registry = EntityRegistry()
        self.world_system = WorldSystem(entity_registry=self.entity_registry,
                                        width=self.config.width,
                                        height=self.config.height)
        self.corruption = CorruptionSystem(
                            entity_registry=self.entity_registry,
                            base_entities=self.world_system.entities,
                            tick_rate=300)

        self.renderer = Renderer(
                            world=self.world_system.get_readable_world(),
                            tick_rate=1,
                            should_render=should_render)
        super().__init__()

    def _load_config(self, config_file_name: Optional[str]):
        if config_file_name is None:
            return load_config()
        else:
            return load_config(config_file_name)

    def run(self):
        while self.current_tick <= self.config.runtime_ticks:
            self.corruption.update(self.current_tick)
            self.world_system.update(self.current_tick)

            self.renderer.update(self.current_tick)

            self.current_tick += 1
        self.renderer.teardown()
