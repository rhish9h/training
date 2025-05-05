# 📘 Module 2: API Development with FastAPI

| Submodule                             | Study | Project | Difficulty |
| ------------------------------------- | ----- | ------- | ---------- |
| 2.1 FastAPI Basics                    | 6h    | 4h      | I          |
| 2.2 Dependency Injection & Middleware | 6h    | 4h      | I          |
| 2.3 Background Tasks & Lifespan       | 4h    | 3h      | I          |
| 2.4 Authentication & OAuth2           | 6h    | 5h      | A          |

### 2.1 FastAPI Basics

| Item               | Description                          | Learning Objectives                        | Micro-Project                       | Study | Build | Level |
| ------------------ | ------------------------------------ | ------------------------------------------ | ----------------------------------- | ----- | ----- | ----- |
| 2.1.1 Routing      | Define API endpoints with decorators | - Path parameters, request/response models | CRUD API for simple note app        | 2h    | 1.5h  | I     |
| 2.1.2 Pydantic v2  | Data validation                      | - Custom validators, response schemas      | Pydantic-powered data entry service | 2h    | 1.5h  | I     |
| 2.1.3 OpenAPI Docs | Auto-generated API docs              | - Explore Swagger and ReDoc                | Self-documented JSON API            | 2h    | 1h    | I     |

**Branch Project 2.1:** Notes API – CRUD application with fully typed models, validation, and OpenAPI docs.

### 2.2 Dependency Injection & Middleware

| Item                    | Description                | Learning Objectives            | Micro-Project                            | Study | Build | Level |
| ----------------------- | -------------------------- | ------------------------------ | ---------------------------------------- | ----- | ----- | ----- |
| 2.2.1 DI with Depends   | Manage logic reuse         | - Clean controller design      | Authenticated route using custom Depends | 2h    | 1.5h  | I     |
| 2.2.2 Custom Middleware | Pre-/post-processing logic | - Inject headers, log requests | Middleware to log and tag requests       | 2h    | 1.5h  | I     |
| 2.2.3 CORS & Headers    | API integration basics     | - Cross-origin handling        | CORS-enabled recipe API                  | 2h    | 1h    | I     |

**Branch Project 2.2:** Interceptor API – Middleware-enhanced service with DI-based route protection.

### 2.3 Background Tasks & Lifespan

| Item                   | Description              | Learning Objectives                      | Micro-Project                          | Study | Build | Level |
| ---------------------- | ------------------------ | ---------------------------------------- | -------------------------------------- | ----- | ----- | ----- |
| 2.3.1 Background Tasks | Post-response processing | - Schedule fire-and-forget tasks         | Email-sender API with delayed delivery | 2h    | 1.5h  | I     |
| 2.3.2 App Lifespan     | Setup/teardown hooks     | - Init database pool, external resources | Service with startup/cleanup messages  | 2h    | 1h    | I     |

**Branch Project 2.3:** Task Queue Stub – API with background job execution and lifecycle-managed dependencies.

### 2.4 Authentication & OAuth2

| Item                 | Description          | Learning Objectives                        | Micro-Project                         | Study | Build | Level |
| -------------------- | -------------------- | ------------------------------------------ | ------------------------------------- | ----- | ----- | ----- |
| 2.4.1 OAuth2 & JWT   | Token-based security | - Secure routes with Bearer token          | Tokenized todo list API               | 3h    | 2h    | A     |
| 2.4.2 Scopes & Roles | Role-based access    | - Protect endpoints using custom scopes    | Role-based user manager               | 2h    | 2h    | A     |
| 2.4.3 Refresh Tokens | Session lifecycle    | - Enable token renewal using refresh flows | Auth service with access/refresh pair | 1h    | 1h    | A     |

**Branch Project 2.4:** Auth Portal API – Full OAuth2 service with login, refresh tokens, and protected endpoints.

**Capstone 2:** Budget Tracker API – A FastAPI-based financial management API with account auth, expense CRUD, rate limits, and docs.
