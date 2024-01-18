from factorio_simulation.configs.config import load_config
from factorio_simulation.components.tile_content import TileContent
from factorio_simulation.entities.entity_registry import EntityRegistry
from factorio_simulation.entities.inserter import Inserter
from factorio_simulation.systems.world_system import WorldSystem
from factorio_simulation.systems.interaction_movement_system import InteractionMovementSystem
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
        inserter = Inserter(x=1, y=1)
        self.world_system.set_tile_content(inserter.get_component(TileContent), 1, 1)
        self.interaction_system = InteractionMovementSystem(
                                    entity_registry=self.entity_registry,
                                    world=self.world_system.get_readable_world())
        self.interaction_system.add_entity(inserter)

        self.corruption = CorruptionSystem(
                            entity_registry=self.entity_registry,
                            base_entities=self.world_system.entities,
                            tick_rate=100)

        self.renderer = Renderer(
                            world=self.world_system.get_readable_world(),
                            tick_rate=1,
                            should_render=should_render)
        super().__init__()

    def _load_config(self, config_file_name: Optional[str]):
        return load_config(config_file_name)

    def run(self):
        while self.current_tick <= self.config.runtime_ticks:
            self.corruption.update(self.current_tick)
            self.interaction_system.update(self.current_tick)
            self.world_system.update(self.current_tick)

            self.renderer.update(self.current_tick)

            self.current_tick += 1
        self.renderer.teardown()
