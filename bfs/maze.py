from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
# from generic_search import dfs, bfs, node_to_path

class Cell(str, Enum):
    Empty = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    col: int

class Maze:
    def __init__(self, rows: int = 10, cols: int = 10, sparseness: float = 0.1, start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation( 9, 9)) -> None:
        self._rows: int = rows
        self._cols: int = cols
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: List[List[Cell]] = [[Cell.Empty for _ in range(cols)] for _ in range(rows)]

    