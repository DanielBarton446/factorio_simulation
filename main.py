from factorio_simulation.simulation import world_simulation
import argparse

def _setup_argparse():
    parser = argparse.ArgumentParser(description='Run a factorio simulation')
    parser.add_argument('-c', '--config', type=str, help='Config file to use')
    return parser

def parse_args():
    args = _setup_argparse().parse_args()
    return args
def main():
    args = parse_args()

    world = world_simulation.WorldSimulation(args.config)

    world.run()


if __name__ == '__main__':
    main()
