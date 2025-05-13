# Micro Project 1.1.1: Refactor Utility Module to 100% MyPy Coverage

## Objective
Apply strict typing to a collection of utility functions to achieve 100% MyPy compliance.

## Project Description
In this micro project, you'll add complete type annotations to an existing utility module containing common helper functions. The goal is to make the module pass `mypy --strict` checks with no errors while maintaining the original functionality.

## Requirements
- Add complete type annotations to all functions in `utils.py`
- Implement at least one `Protocol` to define a contract
- Use generics (`TypeVar`) for at least one flexible function that works with multiple types
- Demonstrate proper variance with covariant/contravariant type parameters
- Ensure all tests pass and the module functions correctly

## Getting Started
1. Review the existing code in `utils.py` to understand the functionality
2. Run the tests to ensure you understand how the functions should behave:
   ```bash
   pytest test_utils.py -v
   ```
3. Run the mypy check to see the current type errors:
   ```bash
   python mypy_check.py
   # or directly
   mypy --strict utils.py
   ```
4. Refactor the code by adding appropriate type annotations
5. Continue running the mypy check until all errors are resolved
6. Ensure all tests still pass after your changes

## Project Structure
- `utils.py` - The utility module to refactor
- `test_utils.py` - Tests to verify functionality
- `mypy_check.py` - Script to run mypy checks with strict settings
- `review_rubric.md` - Evaluation criteria for the completed project

## Learning Goals
- Understand and implement static typing in Python
- Master the use of the typing module features
- Apply Protocols and generics in a practical context
- Learn to use MyPy for type checking

## Tips
- Start by importing the appropriate types from the `typing` module
- Consider what type information each function needs:
  - Parameter types
  - Return types
  - Generic type parameters
- Use `Protocol` to define interfaces rather than concrete types where appropriate
- Pay attention to collection types and their contents
- Think about type variance when designing generic functions

## Expected Output
A fully typed utility module that passes `mypy --strict` checks with no errors while maintaining all original functionality.
