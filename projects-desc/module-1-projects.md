# Module 1: Core Python & Async Foundations - Project Descriptions

## 1.1 Modern Python Typing

### 1.1.1 - Refactor Utility Module to 100% MyPy Coverage
**Objective**: Apply strict typing to a collection of utility functions.

**Description**:
- Create or take an existing utility module with 5-7 common helper functions (string manipulations, data transformations)
- Add complete type annotations with `mypy --strict` compliance
- Implement at least one `Protocol` to define a contract 
- Use generics (`TypeVar`) for a flexible function that works with multiple types
- Demonstrate proper variance with covariant/contravariant type parameters

**Expected Output**: A fully typed utility module that passes `mypy --strict` checks with no errors.

### 1.1.2 - Benchmark Dataclasses vs Pydantic v2
**Objective**: Compare performance and developer experience between standard dataclasses and Pydantic.

**Description**:
- Create identical data models using both dataclasses and Pydantic v2
- Implement JSON serialization/deserialization for both approaches
- Build a benchmarking script that creates/validates 1000 objects
- Measure and compare performance, memory usage, error handling
- Test edge cases with invalid data to observe differences in validation behavior

**Expected Output**: A comparison report with benchmark results and pros/cons analysis.

### 1.1.3 - Transform State Machine with Pattern Matching
**Objective**: Refactor a state-based system using Python 3.10+ pattern matching.

**Description**:
- Create a simple state machine (e.g., document workflow or transaction processing)
- Implement two versions: traditional if-else chains and modern match-case
- Include complex patterns with guards, OR patterns, and structural patterns
- Demonstrate how pattern matching creates more readable and maintainable code

**Expected Output**: A before/after implementation with performance and readability comparison.

### Branch Project 1.1: Type-Safe FastAPI Stub
**Objective**: Create a small FastAPI service with comprehensive type safety.

**Description**:
- Build a microservice with 3-4 endpoint routes
- Implement Pydantic v2 models for all requests and responses
- Ensure complete MyPy coverage with strict checking
- Use Protocols for dependency injection interfaces
- Implement custom generic types where appropriate
- Document all types with clear docstrings and examples

**Expected Output**: A small but production-quality FastAPI service with 100% type coverage.

## 1.2 Async IO Fundamentals

### 1.2.1 - Async Downloader with Cancellation Logic
**Objective**: Build a downloader that fetches multiple files concurrently with proper error handling.

**Description**:
- Create an async downloader that fetches 5+ files simultaneously
- Implement timeout-based cancellation for hanging downloads
- Handle connection errors gracefully with appropriate status reporting
- Allow user-initiated cancellation that properly closes connections
- Measure and display speed improvements vs sequential downloads

**Expected Output**: A working async downloader CLI tool with progress reporting and cancellation.

### 1.2.2 - Queue-Based File Processor
**Objective**: Create a producer-consumer system using async queues.

**Description**:
- Implement a file watcher (producer) that observes a directory
- Process new files using a pool of worker coroutines (consumers)
- Use semaphores to limit concurrent processing based on system resources
- Maintain an async queue for backlog management
- Implement proper queue size limits with backpressure handling

**Expected Output**: A service that monitors and processes files with controlled concurrency.

### 1.2.3 - Decorator for Blocking Operation Warnings
**Objective**: Detect and report potentially blocking calls in async code.

**Description**:
- Create a decorator that can wrap async functions
- Detect when synchronous I/O or CPU-intensive operations block the event loop
- Log warnings with stack traces and execution time
- Implement optional timeout thresholds for detecting different blocking scenarios
- Create example "bad" functions that demonstrate the detection in action

**Expected Output**: A reusable decorator that helps identify performance issues in async code.

### Branch Project 1.2: Async File Uploader
**Objective**: Build a CLI tool that uploads files concurrently to a mock cloud storage.

**Description**:
- Create a command-line interface for bulk file uploads
- Implement a mock S3-like storage service for testing
- Use async patterns to upload multiple files concurrently
- Implement proper timeout handling and cancellation
- Add connection pooling and rate limiting
- Display real-time progress for each file and overall batch

**Expected Output**: A high-performance file uploader utility with concurrency controls.

## 1.3 Logging & Error Handling

### 1.3.1 - Filterable Structured Logger
**Objective**: Implement a structured JSON logger with context enrichment.

**Description**:
- Set up structlog or loguru for structured JSON logging
- Implement context managers to add request/correlation IDs
- Create filters to target specific events or log levels
- Ensure all logs are machine-parsable with consistent schema
- Demonstrate how logs can be queried and analyzed

**Expected Output**: A configurable logging setup with context propagation and structured output.

### 1.3.2 - Middleware to Log Deep Tracebacks
**Objective**: Enhance error visibility with comprehensive traceback information.

**Description**:
- Build middleware for capturing and formatting detailed exception info
- Integrate with the structured logger from the previous project
- Display execution context for clearer debugging
- Format chained exceptions clearly to show error propagation
- Include optional environment and system info in crash reports

**Expected Output**: Error handling middleware that provides detailed debugging information.

### 1.3.3 - Retry Wrapper for Unstable HTTP Call
**Objective**: Build resilient network operations with advanced retry logic.

**Description**:
- Use tenacity to implement retry logic for flaky API calls
- Configure exponential backoff with jitter
- Implement retry conditions based on specific error types
- Create retry behavior statistics with structured logging
- Include circuit breaker pattern to prevent overwhelming failing services

**Expected Output**: A reliable API client that can handle transient failures gracefully.

### Branch Project 1.3: Robust Uploader
**Objective**: Enhance the async uploader with production-grade reliability features.

**Description**:
- Extend the previous uploader with structured logging
- Add detailed error handling with custom exception hierarchies
- Implement retry logic with exponential backoff
- Create a comprehensive event log for auditing
- Include checksum verification for upload integrity
- Add resume capability for interrupted uploads

**Expected Output**: An enterprise-ready uploader with observability and reliability.

## Module 1 Capstone: Production-Grade Async Uploader

**Objective**: Combine all Module 1 concepts into a complete, production-quality file uploader service.

**Description**:
- Create a fully typed (MyPy --strict) async file upload service
- Implement both CLI and API interfaces (FastAPI)
- Use modern Python patterns and match/case for operation modes
- Support concurrent uploads with configurable rate limiting
- Implement producer/consumer patterns for preprocessing
- Add comprehensive structured logging throughout the pipeline
- Include robust error handling with detailed tracebacks
- Implement intelligent retry logic with circuit breakers
- Add metrics collection for upload performance
- Provide configuration for different storage backends

**Expected Output**: A complete, production-ready file upload service that could be deployed in a real environment, demonstrating mastery of all Module 1 concepts.

**Success Criteria**:
- Passes MyPy strict checks
- Handles errors gracefully at all stages
- Processes files concurrently with proper resource management
- Generates useful structured logs and metrics
- Implements retry logic for transient failures
- Ensures data integrity throughout the upload process
