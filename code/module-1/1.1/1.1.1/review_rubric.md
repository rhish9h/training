# Code Review Rubric for Micro Project 1.1.1

This rubric will be used to evaluate your implementation of the typed utility module. Your code will be assessed on these criteria:

## 1. Type Correctness (40%)

| Criteria | Points | Description |
|----------|--------|-------------|
| MyPy Strict Compliance | 15 | Code passes `mypy --strict` with no errors |
| Type Accuracy | 10 | Types accurately represent function parameters and returns |
| Edge Cases | 10 | Types account for edge cases and special conditions |
| Type Imports | 5 | Appropriate imports from typing module |

## 2. Advanced Typing Features (30%)

| Criteria | Points | Description |
|----------|--------|-------------|
| Protocol Implementation | 10 | At least one Protocol defined and used correctly |
| Generic Types | 10 | Appropriate use of TypeVar and generic types |
| Variance | 10 | Proper implementation of variance (co/contravariant) |

## 3. Code Quality (20%)

| Criteria | Points | Description |
|----------|--------|-------------|
| Readability | 10 | Types enhance rather than obscure code readability |
| Docstrings | 5 | Type information reflected in docstrings |
| Consistency | 5 | Consistent type annotation style throughout |

## 4. Functionality (10%)

| Criteria | Points | Description |
|----------|--------|-------------|
| Test Passing | 5 | All tests continue to pass |
| Behavior Preservation | 5 | Original functionality is preserved |

## Evaluation Guide

- **Excellent (90-100%)**: Complete and correct type annotations with creative use of advanced typing features
- **Good (75-89%)**: Code passes mypy checks with proper typing but may have minor issues in advanced features
- **Satisfactory (60-74%)**: Basic typing is correct but advanced features are not well implemented
- **Needs Improvement (<60%)**: Significant typing errors or incomplete typing coverage

## Example Implementation Highlights to Look For:

1. Use of appropriate collection types (List, Dict, Tuple, etc.)
2. Callable types with proper signature typing
3. Protocol definition that abstracts common behavior
4. TypeVars with appropriate constraints
5. Variance annotations where appropriate
6. Optional/Union types for functions that can return None
7. Type comments where complex expressions could benefit from them
