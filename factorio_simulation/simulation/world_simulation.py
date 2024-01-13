from factorio_simulation.configs.config import load_config
from typing import Optional


class WorldSimulation:
    
    def __init__(self, config_file_name: Optional[str] = None):
        self.config = self._load_config(config_file_name)
        self.current_tick = 0

    def _load_config(self, config_file_name: Optional[str]):
        if config_file_name is None:
            return load_config()
        else:
            return load_config(config_file_name)


    def run(self):
        while self.current_tick < self.config.runtime_ticks:
            self.current_tick += 1
