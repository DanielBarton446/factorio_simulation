from factorio_simulation.utils import CONFIG_DIR
from dataclasses import dataclass
from os import path
import configparser


@dataclass(frozen=True)
class Config:
    tick_rate: int
    runtime_ticks: int
    width: int
    height: int


def load_config(file_name: str = "normal_world.ini"):
    config_file = CONFIG_DIR / file_name
    if not path.exists(config_file):
        raise FileNotFoundError(f"Config file {config_file} does not exist")

    conf_parser = configparser.ConfigParser()
    conf_parser.read(config_file)

    try:
        tick_rate: int = int(conf_parser["simulation"]["tick_rate"])
        runtime: int = int(conf_parser["simulation"]["runtime_ticks"])
        width: int = int(conf_parser["world"]["width"])
        height: int = int(conf_parser["world"]["height"])
    except KeyError:
        raise ValueError(f"Config file {config_file} is missing required values")

    return Config(
        tick_rate=tick_rate, runtime_ticks=runtime, width=width, height=height
    )
