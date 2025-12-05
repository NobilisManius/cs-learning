from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
# from generic_search import dfs, bfs, node_to_path

class Cell(str, Enum):
    Empty = "▢"
    BLOCKED = "▣"
    START = "ø"
    GOAL = ""
    PATH = "•"
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

        self._randomly_fill(sparseness)

    def _randomly_fill(self, sparseness: float):
        for row in range(self._rows):
            for col in range(self._cols):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][col] = Cell.BLOCKED
    
    def __str__(self) -> str:
        output: str = ""
        border = "═" * (self._cols * 2 + 1)
        output += f"╔{border}╗\n"
        for i, row in enumerate(self._grid):
            output += "║ "
            output += " ".join([
                cell.value if MazeLocation(i, j) not in [self.start, self.goal]
                else (Cell.START.value if MazeLocation(i, j) == self.start
                      else "●")
                for j, cell in enumerate(row)
            ])
            output += " ║\n"
        output += f"╚{border}╝"
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.col] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.col))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.col] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.col))
        if ml.col + 1 < self._cols and self._grid[ml.row][ml.col + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.col + 1))
        if ml.col - 1 >= 0 and self._grid[ml.row][ml.col - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.col - 1))
        return locations