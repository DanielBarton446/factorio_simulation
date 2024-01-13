from factorio_simulation.configs.config import load_config


class WorldSimulation:
    
    def __init__(self):
        self.config = self._load_config()

    def _load_config(self, config_file_name: str = 'normal_world.ini'):
        return load_config(config_file_name)

    def run(self):
        print(self.config)
