import argparse

from factorio_simulation.simulation import world_simulation
# from factorio_simulation.simulation import dummy_simulation
from factorio_simulation.utils import get_logger

logger = get_logger(__name__)


def _setup_argparse():
    parser = argparse.ArgumentParser(description="Run a factorio simulation")
    parser.add_argument("-c", "--config", type=str, help="Config file to use")
    parser.add_argument(
        "-x", "--no-render", help="Do not render the simulation", action="store_true"
    )
    return parser


def parse_args():
    args = _setup_argparse().parse_args()
    return args


def main():
    args = parse_args()

    # world = dummy_simulation.DummySimulation(args.config)
    world = world_simulation.WorldSimulation(not args.no_render, args.config)

    logger.info("Starting simulation")
    world.run()
    logger.info("Finished simulation")


if __name__ == "__main__":
    main()
