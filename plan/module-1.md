# 📘 Module 1: Core Python & Async Foundations

| Submodule                    | Study | Project | Difficulty |
| ---------------------------- | ----- | ------- | ---------- |
| 1.1 Modern Python Typing     | 6h    | 3h      | B–I        |
| 1.2 Async IO Fundamentals    | 7h    | 3h      | I          |
| 1.3 Logging & Error Handling | 3h    | 2h      | I          |

### 1.1 Modern Python Typing

| Item                              | Description                                 | Learning Objectives                                           | Micro-Project                                 | Study | Build | Level |
| --------------------------------- | ------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------- | ----- | ----- | ----- |
| 1.1.1 MyPy + Type Hints           | Use `mypy --strict`, generics, and variance | - Add type coverage<br>- Understand Protocols and contracts   | Refactor utility module to 100% MyPy coverage | 2h    | 1h    | I     |
| 1.1.2 Dataclasses vs. Pydantic v2 | Compare runtime & validation approaches     | - Serialize/validate JSON<br>- Evaluate dev ergonomics        | Benchmark 1000 object parses with both        | 2h    | 1h    | I     |
| 1.1.3 Pattern Matching            | Use match-case idioms from Python 3.10+     | - Replace legacy `if-else` chains with modern matching syntax | Transform state machine with `match`          | 2h    | 1h    | B–I   |

**Branch Project 1.1:** Type-Safe FastAPI Stub – Build a FastAPI microservice with strict typing and Pydantic v2 validation.

### 1.2 Async IO Fundamentals

| Item                          | Description                               | Learning Objectives                                      | Micro-Project                             | Study | Build | Level |
| ----------------------------- | ----------------------------------------- | -------------------------------------------------------- | ----------------------------------------- | ----- | ----- | ----- |
| 1.2.1 Coroutines & Tasks      | Understand `async/await` and cancellation | - Parallel execution<br>- Handling timeouts/cancellation | Async downloader with cancellation logic  | 3h    | 1.5h  | I     |
| 1.2.2 Async Queues/Semaphores | Manage concurrency control mechanisms     | - Rate-limiting<br>- Producer-consumer patterns          | Queue-based file processor                | 2h    | 1h    | I     |
| 1.2.3 Blocking Call Detection | Avoid sync bottlenecks in async code      | - Identify and log blocking operations                   | Decorator for blocking operation warnings | 2h    | 0.5h  | I     |

**Branch Project 1.2:** Async File Uploader – CLI that uploads files concurrently to a mock S3 bucket with retry, timeout, and circuit breaker.

### 1.3 Logging & Error Handling

| Item                     | Description                       | Learning Objectives                                         | Micro-Project                        | Study | Build | Level |
| ------------------------ | --------------------------------- | ----------------------------------------------------------- | ------------------------------------ | ----- | ----- | ----- |
| 1.3.1 Structured Logging | Use `structlog` or `loguru`       | - Create structured JSON logs<br>- Inject trace/context IDs | Filterable structured logger         | 1.5h  | 1h    | I     |
| 1.3.2 Rich Tracebacks    | Improve debugging with visibility | - Enhanced exception traces<br>- Chained error logging      | Middleware to log deep tracebacks    | 1h    | 0.5h  | I     |
| 1.3.3 Retry Logic        | Use `tenacity` for resilience     | - Retry on transient faults<br>- Exponential backoff        | Retry wrapper for unstable HTTP call | 0.5h  | 0.5h  | I     |

**Branch Project 1.3:** Robust Uploader – Add structured logging, exception handling, and retry logic to the uploader service.

**Capstone 1:** Production-Grade Async Uploader – Combine all submodules into an async file upload tool with error handling, type safety, logging, retries, and concurrency control.
