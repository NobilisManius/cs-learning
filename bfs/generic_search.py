from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop
from abc import ABC, abstractmethod

T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

class Comparable(Protocol):
    def __gt__(self, other: Any) -> bool:
        return (not self < other) and self != other
    def __ge__(self, other: Any) -> bool:
        return not self < other
    def __le__(self, other: Any) -> bool:
        return self < other or self == other
    def __lt__(self, other: Any) -> bool:
        return self < other
    def __eq__(self, other: Any) -> bool:
        return self == other
    def __ne__(self, other: Any) -> bool:
        return self != other
    def __gt__(self, other: Any) -> bool:
        return not self < other and self != other
    def __ge__(self, other: Any) -> bool:
        return not self < other
    def __le__(self, other: Any) -> bool:
        return self < other or self == other

    def binary_contains(sequence: Sequence[Comparable], key: Comparable) -> bool:
        low: int = 0
        high: int = len(sequence) - 1
        while low <= high:
            mid: int = (low + high) // 2
            if sequence[mid] < key:
                low = mid + 1
            elif sequence[mid] > key:
                high = mid - 1
            else:
                return True
        return False