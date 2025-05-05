# Module 2: API Development with FastAPI - Project Descriptions

## 2.1 FastAPI Basics

### 2.1.1 - CRUD API for Simple Note App
**Objective**: Create a basic API with full CRUD operations.

**Description**:
- Set up a FastAPI application with appropriate route structure
- Implement endpoints for creating, reading, updating, and deleting notes
- Use path parameters for accessing specific resources
- Create request/response models for data validation
- Implement proper HTTP status codes for different scenarios
- Include error handling for common failure cases

**Expected Output**: A functioning API for note management with appropriate routes and data models.

### 2.1.2 - Pydantic-Powered Data Entry Service
**Objective**: Master Pydantic v2's validation capabilities for API data.

**Description**:
- Build a data entry API with complex validation requirements
- Implement custom validators for business logic rules
- Create nested models with interdependent fields
- Use field constraints for format validation (email, URL, etc.)
- Implement custom error responses for validation failures
- Create models with optional and required fields

**Expected Output**: A robust data validation service using Pydantic v2's features.

### 2.1.3 - Self-Documented JSON API
**Objective**: Create a well-documented API using FastAPI's OpenAPI integration.

**Description**:
- Build an API with comprehensive docstrings and descriptions
- Customize Swagger UI and ReDoc presentation
- Add examples to operations and response models
- Implement response schemas with proper descriptions
- Create grouped tags for organizing endpoints
- Add proper response codes and descriptions

**Expected Output**: A fully documented API with interactive documentation.

### Branch Project 2.1: Notes API
**Objective**: Build a complete CRUD application with FastAPI best practices.

**Description**:
- Create a full-featured notes application API
- Implement comprehensive Pydantic models with validation
- Use proper route organization with versioning
- Create fully typed response models
- Implement pagination for list endpoints
- Add filtering and sorting capabilities
- Include comprehensive API documentation
- Implement proper error handling and status codes

**Expected Output**: A production-quality notes API with full CRUD capabilities.

## 2.2 Dependency Injection & Middleware

### 2.2.1 - Authenticated Route Using Custom Depends
**Objective**: Implement route protection using dependency injection.

**Description**:
- Create a FastAPI dependency for authentication
- Implement bearer token validation logic
- Use the dependency to protect specific routes
- Add error handling for unauthorized or invalid access
- Create nested dependencies for different security levels
- Demonstrate dependency caching vs. non-caching calls

**Expected Output**: A protected API using clean dependency injection patterns.

### 2.2.2 - Middleware to Log and Tag Requests
**Objective**: Create custom middleware for request processing.

**Description**:
- Implement a FastAPI middleware that logs request details
- Add correlation IDs to track requests through the system
- Measure and log response times for performance monitoring
- Tag requests with user agent and client info
- Create middleware-based rate limiting
- Implement request/response header modifications

**Expected Output**: A middleware layer that provides observability for API requests.

### 2.2.3 - CORS-Enabled Recipe API
**Objective**: Set up proper CORS handling for web API integration.

**Description**:
- Create a simple recipe API with typical CRUD operations
- Configure CORS middleware with appropriate settings
- Support credential-based requests from specific origins
- Set up proper headers for browser security
- Test cross-domain requests with a simple frontend
- Handle preflight requests properly

**Expected Output**: An API ready for cross-origin browser integration.

### Branch Project 2.2: Interceptor API
**Objective**: Create an API with advanced middleware and dependency injection.

**Description**:
- Build a service with multiple integrated middleware components
- Implement authentication using custom dependency injection
- Create middleware for logging, metrics, and error handling
- Add request validation and sanitization
- Implement content negotiation for different response formats
- Create dependency-based feature flags
- Add comprehensive request context tracking

**Expected Output**: An API showcasing advanced FastAPI middleware and dependency patterns.

## 2.3 Background Tasks & Lifespan

### 2.3.1 - Email-Sender API with Delayed Delivery
**Objective**: Implement background tasks for post-response processing.

**Description**:
- Create an API that accepts email sending requests
- Implement a background task system for non-blocking processing
- Add delayed sending capability with scheduling options
- Include status tracking for background operations
- Implement error handling and retry logic
- Create an admin endpoint to view task status

**Expected Output**: An API that processes email tasks asynchronously after request completion.

### 2.3.2 - Service with Startup/Cleanup Messages
**Objective**: Use application lifecycle events for resource management.

**Description**:
- Implement FastAPI's lifespan events (startup/shutdown)
- Create database connection pools on application startup
- Set up proper cleanup of external resources on shutdown
- Add health check endpoints that validate connections
- Implement graceful shutdown capability
- Log application lifecycle events

**Expected Output**: A service that properly manages resources throughout its lifecycle.

### Branch Project 2.3: Task Queue Stub
**Objective**: Build an API with background processing and lifecycle management.

**Description**:
- Create a task processing API with background workers
- Implement proper resource management through lifecycle events
- Add task status tracking and result storage
- Create task prioritization and queuing
- Implement cancellation capabilities for running tasks
- Add admin endpoints for monitoring task status
- Create graceful shutdown with task completion

**Expected Output**: A task processing API with background job execution and proper lifecycle management.

## 2.4 Authentication & OAuth2

### 2.4.1 - Tokenized Todo List API
**Objective**: Implement JWT-based authentication for API security.

**Description**:
- Create a todo list API with user-specific data
- Implement JWT token generation and validation
- Secure endpoints using JWT authentication
- Add token expiration and verification
- Create login/logout endpoints
- Implement proper error handling for auth failures

**Expected Output**: A secured to-do list API using JWT authentication.

### 2.4.2 - Role-Based User Manager
**Objective**: Implement role-based access control for API endpoints.

**Description**:
- Create a user management API with different access levels
- Implement role and permission models
- Use OAuth2 scopes to control endpoint access
- Create admin-only and user-level endpoints
- Implement permission checking in dependency functions
- Create a permissions middleware for global checks

**Expected Output**: A user management system with role-based access control.

### 2.4.3 - Auth Service with Access/Refresh Pair
**Objective**: Implement refresh token flows for long-lived sessions.

**Description**:
- Create an authentication service with token refresh
- Implement secure storage for refresh tokens
- Create token rotation on refresh for security
- Add token revocation capabilities
- Implement proper expiry timing for both token types
- Create refresh token reuse detection

**Expected Output**: A complete authentication service with refresh token capability.

### Branch Project 2.4: Auth Portal API
**Objective**: Build a complete OAuth2 authentication service.

**Description**:
- Create a full OAuth2 authentication API
- Implement secure login with proper password handling
- Add support for token-based authentication
- Implement refresh token flows with security features
- Create scope-based authorization for API endpoints
- Add user management capabilities
- Implement secure token storage and validation
- Create comprehensive security headers and protections

**Expected Output**: A production-ready authentication service with OAuth2 compliance.

## Module 2 Capstone: Budget Tracker API

**Objective**: Create a comprehensive financial management API integrating all Module 2 concepts.

**Description**:
- Build a complete budget and expense tracking API with FastAPI
- Implement secure user authentication with OAuth2/JWT
- Create role-based access control for shared accounts
- Add comprehensive data validation with Pydantic v2
- Implement middleware for logging, metrics, and security
- Create background tasks for notifications and reports
- Use dependency injection for clean controller design
- Implement proper resource lifecycle management
- Add rate limiting for API protection
- Create comprehensive API documentation
- Implement transaction support for financial operations
- Add filtering, sorting, and pagination for data queries
- Create expense categorization and budget tracking
- Implement proper error handling and status codes

**Expected Output**: A production-ready budget tracking API that demonstrates mastery of all Module 2 FastAPI concepts.

**Success Criteria**:
- Complete user authentication and authorization system
- Proper data validation and error handling
- Background processing for reports and notifications
- Comprehensive API documentation
- Clean dependency-based architecture
- Proper middleware implementation for cross-cutting concerns
