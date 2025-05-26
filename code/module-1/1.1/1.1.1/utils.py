"""
Utility functions that need to be refactored with proper type annotations.

This module contains common helper functions for string manipulation,
data transformation, and other utilities. Your task is to add type annotations
to make this module pass mypy --strict checks.

TODO:
1. Add type annotations to all functions
2. Implement at least one Protocol to define a contract
3. Use generics (TypeVar) for flexible functions
4. Demonstrate proper variance with covariant/contravariant type parameters
"""

# Import the relevant typing modules when you start refactoring
from typing import List, Callable, Sequence, TypeVar, Dict, Union, Optional, Any, Set, Protocol, Generic

T = TypeVar("T")

class Stringable(Protocol):
    def __str__(self) -> str:
        ...

def join_strings(items: List[Stringable], separator: str=" ") -> str:
    """Join a list of items into a single string with the given separator."""
    return separator.join(str(item) for item in items)


def filter_items(items: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """Filter items based on a predicate function."""
    return [item for item in items if predicate(item)]


IntOrStr = TypeVar("IntOrStr", int, str)
def transform_values(data: Dict[str, IntOrStr], transformer: Callable[[IntOrStr], IntOrStr]) -> Dict[str, IntOrStr]:
    """Apply a transformer function to all values in a dictionary."""
    return {key: transformer(value) for key, value in data.items()}

T_co = TypeVar("T_co", covariant=True)

class FirstFinder(Generic[T_co]):
    def find_first(self, items: Sequence[T_co], predicate: Callable[[T_co], bool]) -> Optional[T_co]:
        for item in items:
            if predicate(item):
                return item
        return None

def find_first(items: List[IntOrStr], predicate: Callable[[IntOrStr], bool]) -> Optional[IntOrStr]:
    """Find the first item that matches the predicate."""
    first_finder: FirstFinder[IntOrStr] = FirstFinder()
    return first_finder.find_first(items, predicate)


def group_by(items: List[T], key_func: Callable[[T], IntOrStr]) -> Dict[IntOrStr, List[T]]:
    """Group items by a key function."""
    result: Dict[IntOrStr, List[T]] = {}
    for item in items:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


def safe_get(data: Optional[Dict[IntOrStr, Any]], keys: List[IntOrStr], default: Optional[IntOrStr]=None) -> Optional[IntOrStr]:
    """Safely get a nested value from a dictionary."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current if isinstance(current, (int, str)) else default


def deduplicate(items: List[T]) -> List[T]:
    """Remove duplicates while preserving order."""
    seen: Set[T] = set()
    result: List[T] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
