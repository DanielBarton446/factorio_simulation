from factorio_simulation.utils import CONFIG_DIR
from dataclasses import dataclass
import configparser


@dataclass(frozen=True)
class Config:
    tick_rate: int


def load_config(file_name: str = 'normal_world.ini'):
    config_file = CONFIG_DIR / file_name
    config = configparser.ConfigParser()
    config.read(config_file)

    tick_rate: int = int(config['simulation']['tick_rate'])

    return Config(tick_rate=tick_rate)
