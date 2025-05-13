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


def join_strings(items, separator=" "):
    """Join a list of items into a single string with the given separator."""
    return separator.join(str(item) for item in items)


def filter_items(items, predicate):
    """Filter items based on a predicate function."""
    return [item for item in items if predicate(item)]


def transform_values(data, transformer):
    """Apply a transformer function to all values in a dictionary."""
    return {key: transformer(value) for key, value in data.items()}


def find_first(items, predicate):
    """Find the first item that matches the predicate."""
    for item in items:
        if predicate(item):
            return item
    return None


def group_by(items, key_func):
    """Group items by a key function."""
    result = {}
    for item in items:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


def safe_get(data, keys, default=None):
    """Safely get a nested value from a dictionary."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def deduplicate(items):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
