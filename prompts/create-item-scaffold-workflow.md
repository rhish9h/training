---
description: Generate complete scaffolding for a new tutorial item, adapting to project type (Python, Web, Frontend, etc.) while maintaining consistent structure, docs, tests, and rubrics following the 1.1.1 pattern.
---

Follow this guide to create scaffolding for training modules. Use context7 MCP for documentation when available or web search if unavailable.

## Context
- Project Overview: [Refer to README.md]
- Training Plan: [Refer to plan/]
- Project Descriptions: [Refer to projects-desc/]
- Learning Resources: [Refer to learning-resources/]
- Example Structure: [Refer to code/module-1/1.1/1.1.2/]

## 1. Directory Structure
Create project using this exact pattern:
```
code/module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM}/
```

### Project Type Templates:

**A. Python Core (1.1.1 style)**
```
├── README.md               # Learning objectives & instructions
├── {main_file}.py          # Main implementation with TODOs
├── test_{main_file}.py     # Pytest test cases
├── cheatsheet.md           # Key concepts & examples
├── review_rubric.md        # Evaluation criteria
├── mypy_check.py           # Type checking script
└── seed-code-bak/          # Original code backup
```

**B. Web Framework (FastAPI/Flask)**
```
├── README.md               # Instructions
├── app/                    # Application package
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── routes/
├── tests/                  # Test directory
├── cheatsheet.md           # Framework concepts
└── review_rubric.md        # Evaluation criteria
```

**C. Frontend (React)**
```
├── README.md               # Instructions
├── public/                 # Static assets
├── src/                    # Source code
│   ├── components/         # React components
│   └── App.jsx             # Main component
├── package.json            # Dependencies
├── cheatsheet.md           # React concepts
└── review_rubric.md        # Evaluation criteria
```

**D. Database/ORM**
```
├── README.md               # Instructions
├── models.py               # Data models
├── database.py             # DB connection
├── migrations/             # Schema migrations
├── tests/                  # Test directory
├── cheatsheet.md           # ORM concepts
└── review_rubric.md        # Evaluation criteria
```

**E. Message Queue/Kafka**
```
├── README.md               # Instructions
├── producer.py             # Event producer
├── consumer.py             # Event consumer
├── docker-compose.yml      # Local setup
├── tests/                  # Test directory
├── cheatsheet.md           # Messaging concepts
└── review_rubric.md        # Evaluation criteria
```

## 2. Common Components

### Required Files
- **README.md**: Task description, objectives, prerequisites, instructions, expected outcomes, **Implementation Checklist** (checkbox list that references every class/function the learner must implement).
- **Main Code File(s)**: *Skeleton-only* code. Provide class/function signatures and docstrings that describe required fields/logic, but **do not** implement bodies. Insert `# TODO` markers and raise `NotImplementedError` or use `...` so learners fill in the logic themselves.
- **Tests**: Comprehensive cases with assertions and edge cases. Use `pytest.skip()` for tests tied to later milestones.
- **Cheatsheet.md**: Key concepts, snippets, patterns, documentation links
- **Review Rubric**: Evaluation criteria with point distribution

### Technology-Specific Requirements
- **Python**: Type hints, mypy --strict compliance, docstrings
- **JavaScript**: Strong typing (TypeScript/JSDoc), ESLint config
- **APIs**: OpenAPI documentation, status code handling
- **Database**: Schema diagrams, migration strategy
- **Frontend**: Responsive design, accessibility

### Quality Standards
- **Skeleton Code**: Starter files must contain only signatures/docstrings and TODOs—no completed business logic.
- **Testing**: Appropriate framework (pytest, Jest, httpx)
- **Documentation**: Clear objectives, instructions, and implementation checklist
- **Error Handling**: Proper exception handling
- **Backup**: Always create seed-code-bak with original (skeleton) code

## 3. Verification Checklist
- [ ] Follows exact module-{MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}/{MOD_NUM}.{SUB_MOD_NUM}.{ITEM_NUM} pattern
- [ ] README includes an accurate Implementation Checklist
- [ ] Starter code contains only skeletons (no completed logic)
- [ ] All required files created for project type
- [ ] Tests run successfully with appropriate framework
- [ ] Quality checks pass (linting, type checking)
- [ ] Documentation complete and accurate
- [ ] Seed code properly backed up
- [ ] Verification scripts included (mypy_check.py for Python)
- [ ] Uses best practices for target technology