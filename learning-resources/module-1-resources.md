# Module 1: Core Python & Async Foundations - Learning Resources

## 1.1 Modern Python Typing

### 1.1.1 - Refactor Utility Module to 100% MyPy Coverage

#### Core Concepts
- Python type annotations fundamentals
- MyPy strict mode configuration
- Python Protocols for structural typing
- Generics with TypeVar
- Covariance and contravariance in type systems

#### Search Terms
- "Python type hints tutorial"
- "mypy --strict mode configuration"
- "Python Protocol vs ABC examples"
- "Python TypeVar generic functions"
- "Covariance contravariance Python typing"
- "Real-world Python type annotation examples"

#### Suggested Learning Path
1. **Basic Type Annotations** (1-2 hours)
   - Learn Python's typing syntax
   - Understand basic types (int, str, List, Dict, etc.)
   - Practice with function annotations

2. **MyPy Configuration** (1 hour)
   - Set up MyPy in a project
   - Configure strict mode
   - Understand error messages and how to resolve them

3. **Protocols & Structural Typing** (2 hours)
   - Understand the difference between nominal and structural typing
   - Learn how to define and use Protocols
   - Compare with Abstract Base Classes

4. **Generics with TypeVar** (1-2 hours)
   - Basic generics implementation
   - Create functions that work with multiple types
   - Learn to use bounds and constraints

5. **Variance Concepts** (1-2 hours)
   - Understand variance principles
   - Implement covariant and contravariant type parameters
   - Apply variance in real-world scenarios

#### Recommended Resources

**Official Documentation**
- [Python typing module documentation](https://docs.python.org/3/library/typing.html)
- [MyPy documentation](https://mypy.readthedocs.io/en/stable/)
- [PEP 544 - Protocols](https://peps.python.org/pep-0544/)
- [PEP 483 - The Theory of Type Hints](https://peps.python.org/pep-0483/)

**Articles & Tutorials**
- [Real Python - Python Type Checking Guide](https://realpython.com/python-type-checking/)
- [Python Type Checking (Guide) - Adam Johnson](https://adamj.eu/tech/2021/05/16/python-type-hints-how-to-use-them/)
- [Understanding Type Variance in Python](https://www.devgem.io/posts/understanding-type-variance-in-python-protocols-contravariance-and-type-checkers)

**YouTube Videos**
- [mCoding - "Python Protocols - The Complete Guide"](https://www.youtube.com/watch?v=YepmpU9yEJk)
- [ArjanCodes - "How to Use Python's typing Module"](https://www.youtube.com/watch?v=QORvB-_mbZ0)
- [PyCon 2020 - "Static Typing in Python"](https://www.youtube.com/watch?v=ST33zDM9vOE)

**GitHub Repositories**
- [typeshed](https://github.com/python/typeshed) - Collection of library stubs for Python
- [mypy](https://github.com/python/mypy) - Optional static typing for Python
- [python/typing](https://github.com/python/typing) - Prototype implementation of typing module

---

### 1.1.2 - Benchmark Dataclasses vs Pydantic v2

#### Core Concepts
- Python dataclasses functionality and features
- Pydantic v2 data validation and serialization
- Performance benchmarking techniques
- JSON serialization/deserialization in Python
- Edge case validation and error handling

#### Search Terms
- "Python dataclasses vs Pydantic v2"
- "Pydantic v2 benchmarks performance"
- "Dataclasses JSON serialization"
- "Python benchmarking libraries"
- "Pydantic v2 validation features"
- "Dataclasses field customization"

#### Suggested Learning Path
1. **Python Dataclasses Fundamentals** (1 hour)
   - Learn basic dataclass creation and usage
   - Understand field options and customization
   - Explore built-in methods and behaviors

2. **Pydantic v2 Features** (1-2 hours)
   - Learn model creation and validation
   - Understand Pydantic's validation rules
   - Explore schema generation capabilities

3. **JSON Serialization Techniques** (1 hour)
   - Standard library approaches (json module)
   - Dataclasses serialization methods
   - Pydantic serialization features

4. **Benchmarking Methods** (1 hour)
   - Python's timeit module
   - Memory profiling tools
   - Creating fair benchmarks

5. **Error Handling & Edge Cases** (1 hour)
   - Testing with invalid data
   - Comparing error reporting
   - Handling complex validation scenarios

#### Recommended Resources

**Official Documentation**
- [Python dataclasses documentation](https://docs.python.org/3/library/dataclasses.html)
- [Pydantic v2 documentation](https://docs.pydantic.dev/latest/)
- [Python timeit documentation](https://docs.python.org/3/library/timeit.html)

**Articles & Tutorials**
- [Real Python - Python's dataclasses](https://realpython.com/python-data-classes/)
- [Pydantic v2 Migration Guide](https://docs.pydantic.dev/latest/migration/)
- [Python Memory Profiling Guide](https://pythonspeed.com/articles/memory-profiling-python/)

**YouTube Videos**
- [mCoding - "Dataclasses in Python"](https://www.youtube.com/watch?v=vBH6GRJ1REM)
- [ArjanCodes - "Pydantic: The Most Useful Library Nobody Teaches"](https://www.youtube.com/watch?v=Vj-iU-8_xLs)
- [PyCon 2023 - "What's New in Pydantic v2"](https://www.youtube.com/watch?v=AQzJA9V7Qlg)

**GitHub Repositories**
- [pydantic/pydantic](https://github.com/pydantic/pydantic) - Data validation using Python type hints
- [benchmark-python-serializers](https://github.com/voidfiles/benchmark-python-serializers) - Example benchmarks for Python serializers

---

### 1.1.3 - Transform State Machine with Pattern Matching

#### Core Concepts
- Python 3.10+ pattern matching syntax
- State machine design patterns
- Structural pattern matching vs if-else chains
- Guard patterns and OR patterns
- Code readability and maintainability metrics

#### Search Terms
- "Python 3.10 pattern matching tutorial"
- "match case Python state machine example"
- "Python structural pattern matching guards"
- "Python match case vs if-else performance"
- "State machine implementation Python"
- "Python pattern matching complex patterns"

#### Suggested Learning Path
1. **Pattern Matching Basics** (1 hour)
   - Learn match-case syntax
   - Understand different pattern types
   - Compare with if-else chains

2. **State Machine Fundamentals** (1 hour)
   - Understand state machine concepts
   - Learn implementation patterns in Python
   - Explore state transitions and events

3. **Advanced Pattern Matching** (1-2 hours)
   - Guard patterns with if conditions
   - OR patterns for multiple matches
   - Structural patterns for complex objects

4. **Refactoring Techniques** (1 hour)
   - Strategies for converting if-else to match-case
   - Maintaining behavior during refactoring
   - Testing refactored code

5. **Performance & Readability Analysis** (1 hour)
   - Measuring execution performance
   - Evaluating code readability
   - Documenting improvements

#### Recommended Resources

**Official Documentation**
- [Python 3.10 Pattern Matching Tutorial](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- [PEP 636 - Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)
- [PEP 634 - Structural Pattern Matching: Specification](https://peps.python.org/pep-0634/)

**Articles & Tutorials**
- [Real Python - Pattern Matching Tutorial](https://realpython.com/python310-pattern-matching/)
- [State Machine in Python: Implementation with Examples](https://medium.com/@joaomcteixeira/implement-state-machines-in-a-pythonic-way-7d27bc35e328)
- [Pattern Matching in Python: A Case Study](https://towner.dev/p/pattern-matching-in-python-a-case-study/)

**YouTube Videos**
- [mCoding - "Pattern Matching in Python 3.10"](https://www.youtube.com/watch?v=ASRqxDGutpA)
- [PyConUS - "Modern Python: Pattern Matching"](https://www.youtube.com/watch?v=2zxZr0bIZrs)
- [ArjanCodes - "State Pattern in Python"](https://www.youtube.com/watch?v=kbIvK3a8CJQ)

**GitHub Repositories**
- [python/cpython](https://github.com/python/cpython/blob/main/Lib/test/test_patma.py) - CPython pattern matching tests
- [pytransitions/transitions](https://github.com/pytransitions/transitions) - Lightweight state machine implementation

---

### Branch Project 1.1: Type-Safe FastAPI Stub

#### Core Concepts
- FastAPI fundamentals and request handling
- Type-safe API development with Pydantic
- Dependency injection with Protocols
- Generic types in web API context
- Documentation with type annotations

#### Search Terms
- "FastAPI type annotations tutorial"
- "Pydantic models FastAPI example"
- "Python Protocol dependency injection"
- "Type-safe FastAPI application"
- "FastAPI generic types"
- "Pydantic v2 FastAPI integration"

#### Suggested Learning Path
1. **FastAPI Fundamentals** (1-2 hours)
   - Learn basic FastAPI setup
   - Understand request and response handling
   - Explore path and query parameters

2. **Pydantic Integration** (1 hour)
   - Create request and response models
   - Implement validation rules
   - Generate API documentation from types

3. **Dependency Injection** (1-2 hours)
   - Learn FastAPI dependency system
   - Implement Protocol-based dependencies
   - Create testable service interfaces

4. **Generic API Endpoints** (1 hour)
   - Implement generic CRUD operations
   - Create reusable API components
   - Apply type safety to generic endpoints

5. **Documentation & Testing** (1 hour)
   - Generate OpenAPI documentation
   - Write type-safe tests
   - Validate type consistency

#### Recommended Resources

**Official Documentation**
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Pydantic v2 with FastAPI](https://docs.pydantic.dev/latest/integrations/fastapi/)
- [Python typing Protocol documentation](https://docs.python.org/3/library/typing.html#typing.Protocol)

**Articles & Tutorials**
- [TestDriven.io - FastAPI with Python: Creating Robust APIs](https://testdriven.io/blog/fastapi-crud/)
- [Towards Data Science - Building a Type-Safe API with FastAPI](https://towardsdatascience.com/build-a-type-safe-python-api-using-fastapi-and-pydantic-367c81b952ce)
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)

**YouTube Videos**
- [FastAPI Tutorial Series - Patrick Loeber](https://www.youtube.com/watch?v=7t2alSnE2-I)
- [ArjanCodes - "Dependency Injection in Python"](https://www.youtube.com/watch?v=oHSFKbmRPf8)
- [Pretty Printed - "FastAPI Tutorial"](https://www.youtube.com/watch?v=cw46MSAeUIY)

**GitHub Repositories**
- [tiangolo/fastapi](https://github.com/tiangolo/fastapi) - FastAPI framework
- [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) - Project generator for FastAPI

## 1.2 Asyncio Patterns

### 1.2.1 - Async API Client

#### Core Concepts
- Asyncio fundamentals
- HTTP clients with async capabilities
- Exception handling in async context
- Task management and concurrency control
- Timeouts and cancellation

#### Search Terms
- "Python asyncio tutorial"
- "Async HTTP client Python example"
- "aiohttp vs httpx comparison"
- "Python asyncio error handling patterns"
- "Async context manager Python"
- "Rate limiting async Python requests"

#### Suggested Learning Path
1. **Asyncio Basics** (1-2 hours)
   - Understand async/await syntax
   - Learn coroutine concepts
   - Explore event loop behavior

2. **Async HTTP Clients** (1 hour)
   - Compare aiohttp, httpx, and other libraries
   - Learn request/response patterns
   - Understand session management

3. **Error Handling** (1 hour)
   - Implement try/except in async context
   - Learn about exception propagation
   - Create error handling policies

4. **Concurrency Control** (1-2 hours)
   - Manage multiple concurrent requests
   - Use semaphores for rate limiting
   - Implement backoff strategies

5. **Timeouts & Cancellation** (1 hour)
   - Handle request timeouts
   - Implement proper cancellation
   - Create graceful shutdown

#### Recommended Resources

**Official Documentation**
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)
- [aiohttp documentation](https://docs.aiohttp.org/en/stable/)
- [httpx documentation](https://www.python-httpx.org/)

**Articles & Tutorials**
- [Real Python - Async IO in Python](https://realpython.com/async-io-python/)
- [Practical Python Asyncio Guide](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-1.html)
- [Robust Python Asyncio](https://pythonspeed.com/articles/robust-python-asyncio/)

**YouTube Videos**
- [PyCon 2021 - "Asyncio Patterns"](https://www.youtube.com/watch?v=2IW-ZEui4h4)
- [mCoding - "Python Asyncio: The Complete Guide"](https://www.youtube.com/watch?v=t5Bo1Je9EmE)
- [ArjanCodes - "Async Python: 6 Surprise Pitfalls"](https://www.youtube.com/watch?v=udbV0Qtt_IE)

**GitHub Repositories**
- [python/asyncio](https://github.com/python/asyncio) - Asyncio library development
- [aio-libs/aiohttp](https://github.com/aio-libs/aiohttp) - Async HTTP client/server
