"""
Tests for the utils module that verify both functionality and type coverage.

These tests not only check that functions work correctly but also serve as
examples of how the typed API should be used.
"""

import pytest
from typing import Protocol, TypeVar, List, Dict, Callable, Any, Optional

from utils import (
    join_strings,
    filter_items,
    transform_values,
    find_first,
    group_by,
    safe_get,
    deduplicate,
)


def test_join_strings():
    # Test both str and int items
    assert join_strings(["hello", "world"]) == "hello world"
    assert join_strings([1, 2, 3], "-") == "1-2-3"


def test_filter_items():
    # Should work with any predicate function compatible with the items
    assert filter_items([1, 2, 3, 4], lambda x: x % 2 == 0) == [2, 4]
    assert filter_items(["a", "ab", "abc"], lambda s: len(s) > 1) == ["ab", "abc"]


def test_transform_values():
    # Should transform dictionary values while preserving keys
    assert transform_values({"a": 1, "b": 2}, lambda x: x * 2) == {"a": 2, "b": 4}
    assert transform_values({"x": "hello"}, lambda s: s.upper()) == {"x": "HELLO"}


def test_find_first():
    # Should find first matching item or return None
    assert find_first([1, 2, 3, 4], lambda x: x > 2) == 3
    assert find_first(["a", "b", "c"], lambda s: s == "z") is None


def test_group_by():
    # Should group items by the key function
    items = [1, 2, 3, 4, 5, 6]
    assert group_by(items, lambda x: x % 2) == {0: [2, 4, 6], 1: [1, 3, 5]}
    
    words = ["apple", "banana", "cherry", "date", "blueberry"]
    assert group_by(words, lambda s: s[0]) == {
        "a": ["apple"],
        "b": ["banana", "blueberry"],
        "c": ["cherry"],
        "d": ["date"],
    }


def test_safe_get():
    # Should safely navigate nested dictionaries
    data = {"a": {"b": {"c": 42}}}
    assert safe_get(data, ["a", "b", "c"]) == 42
    assert safe_get(data, ["a", "b", "d"]) is None
    assert safe_get(data, ["x"], default="not found") == "not found"


def test_deduplicate():
    # Should remove duplicates while preserving order
    assert deduplicate([1, 2, 3, 2, 1, 4]) == [1, 2, 3, 4]
    assert deduplicate(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
