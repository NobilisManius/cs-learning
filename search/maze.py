from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, node_to_path, Node, bfs, astar

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
    

    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.col] = Cell.PATH
        self._grid[self.start.row][self.start.col] = Cell.START
        self._grid[self.goal.row][self.goal.col] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.col] = Cell.Empty
        self._grid[self.start.row][self.start.col] = Cell.START
        self._grid[self.goal.row][self.goal.col] = Cell.GOAL

def euclidean_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        return sqrt((ml.row - goal.row) ** 2 + (ml.col - goal.col) ** 2)
    return distance

def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        return abs(ml.row - goal.row) + abs(ml.col - goal.col)
    return distance

if __name__ == "__main__":
    maze: Maze = Maze()
    print("="*60)
    print("ORIGINAL MAZE:")
    print(maze)

    print("="*60)
    print("DFS SOLUTION:")
    solution1: Optional[Node[MazeLocation]] = dfs(maze.start, maze.goal_test, maze.successors)
    if solution1 is None:
        print("No solution found using DFS")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)

    print("="*60)
    print("BFS SOLUTION:")
    solution2: Optional[Node[MazeLocation]] = bfs(maze.start, maze.goal_test, maze.successors)
    if solution2 is None:
        print("No solution found using DFS")
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        maze.mark(path2)
        print(maze)
        maze.clear(path2)
        
    print("="*60)
    print("ASTAR SOLUTION:")
    solution3: Optional[Node[MazeLocation]] = astar(maze.start, maze.goal_test, maze.successors, euclidean_distance(maze.goal))
    if solution3 is None:
        print("No solution found using A*")
    else:
        path3: List[MazeLocation] = node_to_path(solution3)
        maze.mark(path3)
        print(maze)
        maze.clear(path3)
    
    print("="*60)
    print("ASTAR SOLUTION:")
    solution4: Optional[Node[MazeLocation]] = astar(maze.start, maze.goal_test, maze.successors, manhattan_distance(maze.goal))
    if solution4 is None:
        print("No solution found using A*")
    else:
        path4: List[MazeLocation] = node_to_path(solution4)
        maze.mark(path4)
        print(maze)
        maze.clear(path4)