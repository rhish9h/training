# Create Tutorial Item Scaffolding

> **Important:** Adapt the scaffolding to match the specific project type (Python module, web framework, frontend, etc.) while maintaining consistency with the overall curriculum structure.

## Task
Create a complete tutorial item scaffolding for the specified module and submodule. The scaffolding should follow the established pattern from the 1.1.1 example, including all necessary files and structure. Adapt the scaffolding based on the project type, while maintaining consistent documentation and quality standards.

## Context
- Project Overview: [Refer to README.md]
- Training Plan: [Refer to plan/]
- Project Descriptions: [Refer to projects-desc/]
- Learning Resources: [Refer to learning-resources/]
- Example Structure: [Refer to code/module-1/1.1/1.1.1/]

## Requirements

### 1. Directory Structure
Create the appropriate structure following the exact folder pattern below:

```
code/
└── module-{MOD_NUM}/                 # e.g., module-1
    └── {MOD_NUM}.{SUB_MOD_NUM}/       # e.g., 1.1
        └── {MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM}/  # e.g., 1.1.1
```

#### A. For Python Core Modules (default structure, like 1.1.1):
```
module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM}/
├── README.md
├── {main_file}.py
├── test_{main_file}.py
├── cheatsheet.md
├── review_rubric.md
├── mypy_check.py         # Helper script for verifying type compliance
└── seed-code-bak/        # Directory to store original seed code for reference
   └── {main_file}.py
```

#### B. For Web Framework Modules (FastAPI, Flask):
```
module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM}/
├── README.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── routes/
├── tests/
├── cheatsheet.md
├── review_rubric.md
└── seed-code-bak/
```

#### C. For Frontend Modules (React):
```
module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM}/
├── README.md
├── public/
├── src/
│   ├── components/
│   └── App.jsx
├── package.json
├── cheatsheet.md
├── review_rubric.md
└── seed-code-bak/
```

#### D. For Database & ORM Modules:
```
module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM}/
├── README.md
├── models.py
├── database.py
├── migrations/
├── tests/
├── cheatsheet.md
├── review_rubric.md
└── seed-code-bak/
```

#### E. For Message Queue & Distributed Systems:
```
module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM}/
├── README.md
├── producer.py
├── consumer.py
├── docker-compose.yml
├── tests/
├── cheatsheet.md
├── review_rubric.md
└── seed-code-bak/
```

#### F. For DevOps & Deployment:
```
module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM}/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/
├── app/
├── tests/
├── cheatsheet.md
├── review_rubric.md
└── seed-code-bak/
```

#### G. For AI & ML Modules:
```
module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM}/
├── README.md
├── model.py
├── agent.py
├── prompts/
├── tests/
├── cheatsheet.md
├── review_rubric.md
└── seed-code-bak/
```

### 2. File Contents

> **Adapt based on project type:** While the specific files will vary by project type, all projects should include these core components: documentation, implementation code, tests, and learning resources.

> **Note:** Create a backup of the initial seed code in `seed-code-bak/{main_file}.py` before the user starts modifying it. This preserves the original starter code for reference.

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

#### Test Files
- Comprehensive test cases
- Edge cases
- Clear assertions
- Appropriate testing framework:
  - Python: pytest
  - JavaScript/React: Jest
  - API: requests/httpx
  - Database: fixtures and transactions
- Tests should verify both functionality and (where applicable) type usage patterns

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

#### Verification Scripts
- For Python modules:
  - mypy_check.py to verify type compliance
  - Should run mypy against the main file with --strict
- For JavaScript/TypeScript:
  - eslint configuration
  - tsconfig.json for strict type checking
- For other projects:
  - Appropriate linting/validation scripts
- Clear output of success/failure
- Executable from command line

### 3. Additional Requirements
- Use context7 MCP for latest documentation if available
- If context7 is not available, use web search for documentation
- Technology-specific requirements:
  - **Python modules**: Include type hints and pass mypy --strict
  - **JavaScript/TypeScript**: Use strong typing where applicable
  - **API projects**: Include OpenAPI documentation
  - **Database projects**: Include schema diagrams or ERD
  - **Frontend**: Include responsive design considerations
- Follow best practices for each language/framework
- Include appropriate error handling
- Consider cross-platform compatibility

## Output
Create all necessary files in the correct directory under `code/`. The structure should be consistent with the example in 1.1.1.

## Verification
- [ ] All files created following the appropriate structure for the project type
- [ ] Tests pass with the appropriate testing framework
- [ ] Quality checks pass (type checking, linting, etc.)
- [ ] Documentation complete and accurate for the specific technology
- [ ] Rubric covers all aspects of the task
- [ ] Seed code is backed up
- [ ] Verification scripts properly test the project
- [ ] Structure follows the exact module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM} pattern