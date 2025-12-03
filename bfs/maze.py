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

