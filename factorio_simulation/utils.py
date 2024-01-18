import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CONFIG_DIR = BASE_DIR / 'configs'

# Ideally we would be put in the venv location and not in the project directory
LOG_DIR = BASE_DIR / 'logs'
logging.basicConfig(filename=LOG_DIR / 'factorio_simulation.log',
                    filemode='w', level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
