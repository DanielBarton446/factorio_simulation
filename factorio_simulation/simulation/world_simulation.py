from factorio_simulation.configs.config import load_config
from factorio_simulation.systems.world_system import WorldSystem
from factorio_simulation.systems.corruption_system import CorruptionSystem
from typing import Optional


class WorldSimulation:

    def __init__(self, config_file_name: Optional[str] = None):
        self.config = self._load_config(config_file_name)
        self.current_tick = 0

        self.world_system = WorldSystem(self.config.width, self.config.height)
        self.corruption = CorruptionSystem(self.world_system.entities)
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

            self.current_tick += 1
