# Dataclasses vs Pydantic v2 Cheatsheet

This cheatsheet provides key concepts and code examples for working with both dataclasses and Pydantic v2 models.

## Standard Dataclasses

### Basic Usage

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class User:
    name: str
    age: int
    email: str
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)
    active: bool = True
```

### Key Features

- Part of Python standard library (since 3.7)
- Automatic `__init__`, `__repr__`, `__eq__` methods
- Type annotations for IDE support
- No runtime validation by default
- Works with mypy for static type checking

### Customizing Fields

```python
@dataclass
class AdvancedUser:
    id: int
    username: str
    # Field with default factory
    permissions: List[str] = field(default_factory=lambda: ["read"])
    # Field that is excluded from __init__
    created_at: datetime = field(default_factory=datetime.now, init=False)
    # Field with custom metadata
    email: str = field(metadata={"description": "User's email address"})
    # Field that is excluded from representation
    password: str = field(repr=False)
```

### JSON Serialization

```python
from dataclasses import asdict
import json

# Convert dataclass to dictionary
user_dict = asdict(user)

# Convert to JSON string
user_json = json.dumps(user_dict)

# Custom JSON encoder for complex types
class DataclassEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# Using custom encoder
user_json = json.dumps(asdict(user), cls=DataclassEncoder)
```

### JSON Deserialization

```python
# Manual approach
user_dict = json.loads(user_json)
user = User(**user_dict)

# Helper function
def from_json(json_string, dataclass_type):
    data = json.loads(json_string)
    return dataclass_type(**data)

user = from_json(user_json, User)
```

## Pydantic v2

### Basic Usage

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class User(BaseModel):
    name: str
    age: int
    email: str
    tags: List[str] = []
    metadata: Dict[str, str] = {}
    active: bool = True
```

### Key Features

- Runtime validation
- Data conversion
- JSON schema generation
- Error handling with detailed error messages
- Integration with FastAPI and other frameworks
- Performance optimized in v2 with Rust components

### Validation and Field Constraints

```python
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import List

class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    email: EmailStr
    tags: List[str] = Field(default_factory=list, max_length=10)
    
    @field_validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()
```

### JSON Serialization

```python
# Convert to JSON string
user_json = user.model_dump_json()

# With additional options
user_json = user.model_dump_json(
    indent=2,
    exclude={"metadata"},
    exclude_none=True
)
```

### JSON Deserialization

```python
# Parse JSON string
user = User.model_validate_json(user_json)

# Parse dictionary
user_dict = json.loads(user_json)
user = User.model_validate(user_dict)

# With strict validation
user = User.model_validate(user_dict, strict=True)
```

## Performance Benchmarking

### Time Measurement

```python
import time

def benchmark_function(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

# Usage
result, duration = benchmark_function(create_1000_users)
print(f"Function took {duration:.6f} seconds")
```

### Memory Measurement

```python
import tracemalloc

def measure_memory(func, *args, **kwargs):
    tracemalloc.start()
    result = func(*args, **kwargs)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, peak

# Usage
result, peak_memory = measure_memory(create_1000_users)
print(f"Peak memory usage: {peak_memory / 1024 / 1024:.2f} MB")
```

## Key Differences

| Feature | Dataclasses | Pydantic v2 |
|---------|-------------|-------------|
| Runtime Validation | No (unless custom) | Yes, built-in |
| Performance | Faster instantiation | Validation adds overhead |
| JSON Handling | Manual implementation | Built-in methods |
| Error Handling | Basic | Detailed error messages |
| Schema Generation | No | Yes, with JSON Schema |
| Field Defaults | Uses `field()` | Uses `Field()` or direct assignment |
| Inheritance | Standard Python | Enhanced with model config |
| Use Case | Simple data containers | API data validation |

## Migration Between Approaches

### Dataclass to Pydantic

```python
from dataclasses import dataclass
from pydantic import BaseModel
from pydantic.dataclasses import dataclass as pydantic_dataclass

# Option 1: Convert a dataclass to Pydantic dataclass
@dataclass
class UserDataclass:
    name: str
    age: int

# Create Pydantic-powered dataclass
ValidatedUserDataclass = pydantic_dataclass(UserDataclass)

# Option 2: Create equivalent Pydantic model
class UserModel(BaseModel):
    name: str
    age: int
```

### Pydantic to Dataclass

```python
from dataclasses import dataclass
from pydantic import BaseModel

# Original Pydantic model
class UserModel(BaseModel):
    name: str
    age: int

# Equivalent dataclass
@dataclass
class UserDataclass:
    name: str
    age: int
    
    @classmethod
    def from_pydantic(cls, model: UserModel):
        return cls(**model.model_dump())
```
