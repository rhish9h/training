# Python Typing Cheatsheet

This cheatsheet covers all the typing concepts you'll need for this micro project, from basic annotations to advanced features like Protocols and variance.

## Basic Type Annotations
*Annotations for simple data types and function signatures*

### Variable Annotations
*Adding type hints to variables and class attributes*
```python
# Basic types
name: str = "John"
age: int = 30
is_active: bool = True
price: float = 19.99

# Type annotation without assignment
user_id: int  # Declare type without initialization
```

### Function Annotations
*Type hints for function parameters and return values*
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def multiply(a: int, b: int) -> int:
    return a * b
```

## Collection Types
*Type hints for lists, dictionaries, sets, and tuples*

### Lists
*Type hints for ordered, mutable sequences*
```python
from typing import List

# List of strings
names: List[str] = ["Alice", "Bob", "Charlie"]

# List of integers
numbers: List[int] = [1, 2, 3, 4]

# Empty list that will contain strings
empty_names: List[str] = []
```

### Dictionaries
*Type hints for key-value mappings*
```python
from typing import Dict

# Dictionary mapping strings to integers
ages: Dict[str, int] = {"Alice": 30, "Bob": 25}

# Dictionary mapping strings to any type
values: Dict[str, Any] = {"name": "Alice", "age": 30, "active": True}
```

### Sets and Tuples
*Type hints for unique collections and fixed-length sequences*
```python
from typing import Set, Tuple

# Set of integers
unique_numbers: Set[int] = {1, 2, 3}

# Tuple with specific types for each position
point: Tuple[int, int] = (10, 20)

# Tuple with variable length (all same type)
from typing import Tuple
numbers: Tuple[int, ...] = (1, 2, 3, 4, 5)
```

## Optional and Union Types
*Handling values that can be of multiple types or None*

```python
from typing import Optional, Union

# Optional type (value can be the specified type or None)
def find_user(user_id: int) -> Optional[str]:
    # ... logic to find user
    if user_found:
        return username
    return None

# Union type (value can be one of several types)
def process_data(data: Union[str, bytes, List[int]]) -> None:
    # ... process data of different types
    pass
```

## Callable Types
*Type hints for functions and callable objects*

```python
from typing import Callable

# Function that takes an int and returns a bool
predicate: Callable[[int], bool] = lambda x: x > 0

# Function that takes a string and an int and returns a list of strings
formatter: Callable[[str, int], List[str]] = lambda s, n: [s] * n

# Define a function that accepts a callable
def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))
```

## Type Aliases
*Creating custom names for complex types*

```python
from typing import Dict, List

# Create aliases for complex types
UserId = int
UserData = Dict[str, Union[str, int, bool]]
UsersList = List[UserData]

# Use the aliases
def get_user(user_id: UserId) -> UserData:
    # ...
    pass
```

## Generics with TypeVar
*Creating reusable, type-safe functions and classes*

```python
from typing import TypeVar, List, Callable

# Define a type variable
T = TypeVar('T')  # Unbounded type variable (any type)

# Function that works with any type
def first(items: List[T]) -> Optional[T]:
    return items[0] if items else None

# Bounded type variable (must be a subclass of specified types)
Number = TypeVar('Number', int, float)

def add(a: Number, b: Number) -> Number:
    return a + b
```

## Protocols
*Structural subtyping (duck typing) with static type checking*

```python
from typing import Protocol, List

# Define a Protocol (structural subtyping)
class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool:
        ...

# Function that accepts any type that implements __lt__
def min_value(items: List[Comparable]) -> Comparable:
    current_min = items[0]
    for item in items[1:]:
        if item < current_min:
            current_min = item
    return current_min

# Example of a type that satisfies the protocol without explicitly inheriting
class Score:
    def __init__(self, value: int):
        self.value = value
        
    def __lt__(self, other: 'Score') -> bool:
        return self.value < other.value
```

## Variance

Variance defines how subtypes relate to each other when used in generic containers.

```python
from typing import TypeVar, Generic, List

# Covariant type variable (read-only)
T_co = TypeVar('T_co', covariant=True)

# Contravariant type variable (write-only)
T_contra = TypeVar('T_contra', contravariant=True)

# Example: Producer (covariant) - can return T_co or subclass
class Producer(Generic[T_co]):
    def get(self) -> T_co:
        ...

# Example: Consumer (contravariant) - can accept T_contra or superclass
class Consumer(Generic[T_contra]):
    def put(self, item: T_contra) -> None:
        ...
```

### Variance Example
*Practical demonstration of covariance with a Box container*

```python
from typing import TypeVar, Generic, List

class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass

T_co = TypeVar('T_co', covariant=True)

class Box(Generic[T_co]):
    def __init__(self, item: T_co) -> None:
        self.item = item
    
    def get(self) -> T_co:
        return self.item

# Covariance allows this:
dog_box: Box[Dog] = Box(Dog())
animal_box: Box[Animal] = dog_box  # OK with covariance
```

## Any and Final Types
*Special types for dynamic typing and preventing subclassing*

```python
from typing import Any, Final

# Any type - disables type checking
def process(data: Any) -> None:
    # Type checking is effectively disabled for 'data'
    pass

# Final - value cannot be reassigned
MAX_SIZE: Final[int] = 100
```

## Type Comments (for Python < 3.6)

```python
# Variable type comments
count = 0  # type: int

# Function type comments
def greet(name):
    # type: (str) -> str
    return f"Hello, {name}!"
```

## Type Checking and MyPy

```python
# Ignore type checking for a line
result = some_function()  # type: ignore

# Cast a value to a specific type
from typing import cast
number = cast(int, get_value())
```

## Complete Function Example with TypeVar, Protocol, and Optional

```python
from typing import TypeVar, Protocol, Optional, List

# Define a protocol for filterable items
class Filterable(Protocol):
    def matches(self, criteria: str) -> bool:
        ...

T = TypeVar('T', bound=Filterable)

def filter_items(items: List[T], criteria: str) -> List[T]:
    """Filter a list of items based on whether they match a criteria."""
    return [item for item in items if item.matches(criteria)]

# Example implementation
class User:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
    
    def matches(self, criteria: str) -> bool:
        return criteria in self.name or criteria in self.role

# Using the function
users: List[User] = [User("Alice", "admin"), User("Bob", "user")]
admins = filter_items(users, "admin")  # Returns list with Alice
```

## Practical Tips

1. **Start Simple**: Begin with basic annotations before adding complex types
2. **Check Incrementally**: Run mypy after each function's annotations
3. **Use reveal_type()**: For debugging (mypy will show inferred types)
4. **Type Aliases**: Create aliases for complex types to improve readability
5. **Don't Over-Specify**: If a function works with any type, use TypeVar
6. **Protocols over ABCs**: Use Protocols for more flexible structural typing
7. **Comments**: Add comments explaining complex type constructions

---

## Specific Examples for Utility Functions

Here are examples of how you might type some functions similar to those in your utils.py:

### Example: join_strings

```python
from typing import List, Any, Union, overload

# Simple version
def join_strings(items: List[Any], separator: str = " ") -> str:
    return separator.join(str(item) for item in items)

# Advanced version with overloads for type specificity
@overload
def join_strings(items: List[str], separator: str = " ") -> str: ...

@overload
def join_strings(items: List[Union[int, float]], separator: str = " ") -> str: ...

def join_strings(items: List[Any], separator: str = " ") -> str:
    return separator.join(str(item) for item in items)
```

### Example: filter_items with generics

```python
from typing import TypeVar, List, Callable, Protocol, Any

# With TypeVar and Callable
T = TypeVar('T')
def filter_items(items: List[T], predicate: Callable[[T], bool]) -> List[T]:
    return [item for item in items if predicate(item)]

# With Protocol
class Predicate(Protocol):
    def __call__(self, item: Any) -> bool: ...

def filter_items(items: List[T], predicate: Predicate) -> List[T]:
    return [item for item in items if predicate(item)]
```

### Example: safe_get with nested dictionaries

```python
from typing import Dict, List, TypeVar, Any, Optional

T = TypeVar('T')
def safe_get(data: Dict[str, Any], 
            keys: List[str], 
            default: Optional[T] = None) -> Optional[T]:
    current: Any = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current
```
