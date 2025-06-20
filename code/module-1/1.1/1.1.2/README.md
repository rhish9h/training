# Module 1.1.2: Benchmark Dataclasses vs Pydantic v2

## Objective
Compare performance and developer experience between standard dataclasses and Pydantic v2.

## Learning Objectives
- Understand the differences between Python's built-in dataclasses and Pydantic models
- Learn how to implement JSON serialization/deserialization with both approaches
- Develop benchmarking skills for performance analysis
- Analyze tradeoffs between different data validation approaches
- Evaluate error handling capabilities of both solutions

## Prerequisites
- Python 3.10+
- Understanding of Python type annotations
- Basic knowledge of data models and class structures

## Instructions

### 1. Study Both Data Model Approaches
Begin by exploring both dataclasses from the standard library and Pydantic v2 models.

### 2. Implement Equivalent Models
Create identical data models using both:
- Standard dataclasses with appropriate type hints
- Pydantic v2 models with equivalent validation

### 3. Add Serialization/Deserialization
Implement JSON conversion for both approaches:
- Use `json` module + custom encoding/decoding for dataclasses
- Use Pydantic's built-in serialization methods

### 4. Create Benchmarking Framework
Build a script that:
- Creates/validates 1000 objects for both implementations
- Measures execution time
- Tracks memory usage
- Records validation behavior

### 5. Test Edge Cases
Design test cases with invalid data to observe how each approach handles validation errors.

### 6. Compile Comparison Report
Document your findings in a structured report, including:
- Performance metrics
- Memory consumption
- Error handling capabilities
- Developer experience
- Pros and cons analysis

## Implementation Checklist

Mark each task as you complete it – aim for green ticks across the board before moving on.

- [ ] Define `AddressDataclass` and `PersonDataclass` models in `benchmark.py`  
- [ ] Define `AddressPydantic` and `PersonPydantic` models with validation in `benchmark.py`  
- [ ] Complete methods `to_json` and `from_json` inside `PersonDataclass`  
- [ ] Implement helper / benchmarking functions:
  - `generate_sample_data`
  - `benchmark_creation`
  - `benchmark_serialization`
  - `benchmark_deserialization`
  - `benchmark_validation`
  - `measure_memory_usage`
  - `run_benchmarks`
  - `generate_report`
- [ ] Run `python mypy_check.py` and resolve all type-checking errors  
- [ ] Run `pytest -q` until all tests pass  
- [ ] Produce a short performance comparison report (console printout or `report.md`).

## Running Tests
To execute the tests, run:
```bash
pytest test_benchmark.py
```

## Expected Outcome
A comprehensive comparison demonstrating the strengths and weaknesses of each approach, with supporting benchmark data.
