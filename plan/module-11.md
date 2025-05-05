# 📘 Module 11: Testing & Quality Gates

| Submodule               | Study | Project | Difficulty |
| ----------------------- | ----- | ------- | ---------- |
| 11.1 Unit & Integration | 5h    | 3h      | I          |
| 11.2 Mocking & Fixtures | 4h    | 2h      | I          |
| 11.3 Quality Automation | 5h    | 3h      | I–A        |

### 11.1 Unit & Integration

| Item                     | Description                | Learning Objectives                  | Micro-Project                        | Study | Build | Level |
| ------------------------ | -------------------------- | ------------------------------------ | ------------------------------------ | ----- | ----- | ----- |
| 11.1.1 Pytest Basics     | Setup, assert, fixtures    | - Write and run test suites          | Pytest test suite for FastAPI routes | 2h    | 1.5h  | I     |
| 11.1.2 Integration Tests | Cross-component validation | - Test DB + API + logic interactions | Blog API test with real DB + cleanup | 2h    | 1h    | I     |
| 11.1.3 Parametrize & IDs | Data-driven testing        | - Reuse logic with flexible inputs   | Param test suite for calculator API  | 1h    | 0.5h  | I     |

**Branch Project 11.1:** Blog API Test Suite – Fully covered test set including unit and integration layers.

### 11.2 Mocking & Fixtures

| Item                   | Description                       | Learning Objectives                  | Micro-Project                        | Study | Build | Level |
| ---------------------- | --------------------------------- | ------------------------------------ | ------------------------------------ | ----- | ----- | ----- |
| 11.2.1 unittest.mock   | Replace behavior in unit tests    | - Patch out file/DB/net dependencies | File writer test using mock open()   | 2h    | 1h    | I     |
| 11.2.2 Async Mocking   | Awaitables and coroutine mocks    | - Patch `async def` with async mocks | HTTP client call test                | 1h    | 0.5h  | I     |
| 11.2.3 Fixtures Design | Shared setup with pytest fixtures | - Use reusable setup blocks          | Shared test DB with cleanup fixtures | 1h    | 0.5h  | I     |

**Branch Project 11.2:** Mock Test Lab – Demonstration of mocking, async mocking, and fixture layering.

### 11.3 Quality Automation

| Item                        | Description             | Learning Objectives                       | Micro-Project                        | Study | Build | Level |
| --------------------------- | ----------------------- | ----------------------------------------- | ------------------------------------ | ----- | ----- | ----- |
| 11.3.1 Coverage Tools       | Code coverage reporting | - Track gaps and highlight critical paths | Coverage HTML report for service     | 2h    | 1h    | I     |
| 11.3.2 Linters + Formatters | Style and lint rules    | - Enforce PEP8 + static format            | Pre-commit with Black + Ruff + Isort | 2h    | 1h    | I     |
| 11.3.3 Security Scans       | Automated vuln scans    | - Run Bandit + Secrets detectors          | CI pipeline with secrets scanning    | 1h    | 1h    | A     |

**Branch Project 11.3:** Secure Quality Bot – CI-configured test runner with lint, format, coverage, and Bandit.

**Capstone 11:** Microservice Quality Harness – Full testing + automation setup for a modular FastAPI app with all tools integrated and enforced via CI.
