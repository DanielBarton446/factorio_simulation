from typing import Optional
from factorio_simulation.entities.tile import Tile
from factorio_simulation.systems.system import System
from time import sleep

from numpy.typing import NDArray

import curses
import sys
import signal


class Renderer(System):
    def __init__(self,
                 world: NDArray[Tile],
                 tick_rate: Optional[int] = 1,
                 should_render: bool = True):
        self.should_render: bool = should_render
        self.world: NDArray[Tile] = world
        self.tick_rate: int = tick_rate

        # handle ctrl + c before screwing up the terminal
        signal.signal(signal.SIGINT, Renderer.signal_handler)
        signal.signal(signal.SIGTERM, Renderer.signal_handler)

        self.stdscr = curses.initscr()
        curses.curs_set(0)

        super().__init__()

    @staticmethod
    def signal_handler(signal, frame):
        curses.endwin()
        sys.exit(0)

    def get_tile(self, x: int, y: int) -> Tile:
        """
        Gets the tile at the given coordinates.
        Primarily used for consistency in world access.

        @param x: the cartesian x coordinate of the tile
        @param y: the cartesian y coordinate of the tile
        @retuns the tile at the given coordinates.
        """
        return self.world[y][x]

    def set_tile(self, tile: Tile, x: int, y: int):
        """
        Sets the tile at the given coordinates to the given tile.
        Primarily used for consistency in world access.

        @param x: the cartesian x coordinate of the tile
        @param y: the cartesian y coordinate of the tile
        @param tile: the tile to set at the given coordinates.
        """
        self.world[y][x] = tile

    def render(self):
        for (y, vals) in enumerate(self.world):
            for x, tile in enumerate(vals):
                self.stdscr.addstr(y, x, str(tile))
        self.stdscr.refresh()
        sleep(1 / 60)

    def teardown(self):
        curses.endwin()

    def update(self, current_tick):
        if not self.should_render:
            return

        if current_tick % self.tick_rate == 0:
            self.render()
