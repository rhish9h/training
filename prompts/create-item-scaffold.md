# Create Tutorial Item Scaffolding

## Task
Create a complete tutorial item scaffolding for the specified module and submodule. The scaffolding should follow the established pattern from the 1.1.1 example, including all necessary files and structure.

## Context
- Project Overview: [Refer to README.md]
- Training Plan: [Refer to plan/]
- Project Descriptions: [Refer to projects-desc/]
- Learning Resources: [Refer to learning-resources/]
- Example Structure: [Refer to code/module-1/1.1/1.1.1/]

## Requirements

### 1. Directory Structure
Create the following structure in the appropriate location under `code/`:
```
module-{X}/{Y}.{Z}/{task_name}/
├── README.md
├── {main_file}.py
├── test_{main_file}.py
├── cheatsheet.md
└── review_rubric.md
```

### 2. File Contents

#### README.md
- Clear, concise description of the task
- Learning objectives
- Prerequisites
- Instructions for completing the task
- How to run tests
- Expected outcomes

#### Main Python File
- Initial code with TODOs
- Proper type hints
- Docstrings
- Example implementation (commented out)

#### Test File
- Comprehensive test cases
- Edge cases
- Clear assertions
- Can be run with `pytest`

#### Cheatsheet.md
- Key concepts
- Code snippets
- Common patterns
- Links to official documentation

#### Review Rubric
- Clear criteria for evaluation
- Point distribution
- Categories like:
  - Code Quality
  - Functionality
  - Type Safety
  - Documentation

### 3. Additional Requirements
- Use context7 MCP for latest documentation if available
- If context7 is not available, use web search for documentation
- Include type hints and pass mypy --strict
- Follow Python best practices
- Include error handling where appropriate

## Output
Create all necessary files in the correct directory under `code/`. The structure should be consistent with the example in 1.1.1.

## Verification
- [ ] All files created
- [ ] Tests pass
- [ ] Type checks pass
- [ ] Documentation complete
- [ ] Rubric covers all aspects of the task