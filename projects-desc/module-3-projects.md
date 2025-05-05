# Module 3: Data Persistence – SQL + Graph - Project Descriptions

## 3.1 Async SQLAlchemy

### 3.1.1 - CRUD for Bookstore App
**Objective**: Implement basic async ORM operations with SQLAlchemy.

**Description**:
- Set up async SQLAlchemy with PostgreSQL
- Create data models for books, authors, and categories
- Implement async session management
- Build CRUD operations for all entities
- Add relationship handling between models
- Implement proper connection lifecycle management
- Create a basic FastAPI interface to interact with the database

**Expected Output**: A functioning bookstore API with complete CRUD operations using async SQLAlchemy.

### 3.1.2 - Author-Book Relationship API
**Objective**: Master efficient query loading strategies for related data.

**Description**:
- Build an API that handles author and book relationships
- Implement eager loading with selectinload for related collections
- Add joinedload for single relationships
- Create endpoints that showcase different loading strategies
- Compare and benchmark various loading approaches
- Implement pagination with efficient related data loading

**Expected Output**: An API with optimized queries for retrieving related data efficiently.

### 3.1.3 - Order Checkout Workflow
**Objective**: Implement transactional database operations with proper error handling.

**Description**:
- Create a checkout process with multiple database operations
- Implement proper transaction management
- Add rollback logic for failed operations
- Create nested transaction scenarios
- Implement error handling specific to database constraints
- Add transaction logging for audit purposes

**Expected Output**: A reliable checkout system with proper transaction handling.

### Branch Project 3.1: Library DB API
**Objective**: Build a comprehensive library management API with SQLAlchemy.

**Description**:
- Create a complete library management system with multiple related models
- Implement optimized queries with appropriate loading strategies
- Add transaction support for multi-step operations
- Create complex filtering and search capabilities
- Implement pagination with efficient query design
- Add proper connection pooling and lifecycle management
- Create a comprehensive data access layer with separation of concerns

**Expected Output**: A full-featured library API with efficient data access and relationship handling.

## 3.2 Alembic & Migrations

### 3.2.1 - Version-Controlled Movie Schema
**Objective**: Set up and manage database schema migrations.

**Description**:
- Initialize Alembic for a movie database
- Create initial schema migration
- Set up migration versioning
- Add upgrade and downgrade capabilities
- Implement schema changes through multiple migrations
- Create proper migration documentation

**Expected Output**: A version-controlled movie database schema with proper migration history.

### 3.2.2 - Update Schema with Added Fields
**Objective**: Implement schema evolution using Alembic's autogeneration features.

**Description**:
- Build on an existing database schema
- Add new fields to existing models
- Use Alembic's autogenerate feature to detect changes
- Implement non-destructive schema updates
- Handle data migration alongside schema changes
- Test migration reversibility

**Expected Output**: A seamless schema update process with proper versioning and data handling.

### Branch Project 3.2: Blog Schema History
**Objective**: Create a complete database evolution history for a blog platform.

**Description**:
- Design a blog database with posts, comments, users, and tags
- Implement three distinct evolution steps for the schema
- Create proper migration scripts for each evolution
- Add data migration steps as needed
- Implement version checking in the application
- Create a migration-aware application structure
- Add proper documentation for the migration history

**Expected Output**: A complete blog platform with properly managed schema history and migration controls.

## 3.3 Neo4j & Cypher

### 3.3.1 - Simple Org Chart Graph
**Objective**: Create a basic graph database for organizational relationships.

**Description**:
- Set up Neo4j database connection from Python
- Create nodes for users, departments, and roles
- Establish relationship types for reporting structure
- Implement basic CRUD operations for the graph
- Create visualization of the org structure
- Build basic queries to traverse the organization

**Expected Output**: A functional organization chart using Neo4j with basic graph operations.

### 3.3.2 - Shortest Path for Delegation Chains
**Objective**: Implement advanced graph queries to solve path-finding problems.

**Description**:
- Build a delegation system within an organization
- Implement path-finding queries using Cypher
- Create weighted relationships for delegation priority
- Calculate shortest paths between arbitrary nodes
- Implement traversal with conditional logic
- Create visualizations of delegation paths

**Expected Output**: A delegation resolver that efficiently finds paths in complex organizational structures.

### 3.3.3 - Clean Graph with Safe Merges
**Objective**: Implement graph constraints and ensure data integrity.

**Description**:
- Create uniqueness constraints on key properties
- Implement existence constraints for required properties
- Use MERGE operations for safe node creation
- Create indexes for performance optimization
- Implement integrity checks for relationships
- Build cleaning operations for orphaned nodes

**Expected Output**: A robust graph database with proper constraints, indexes, and safe operations.

### Branch Project 3.3: Delegation Resolver
**Objective**: Create a comprehensive permission delegation system using Neo4j.

**Description**:
- Build a complete user permission delegation system
- Implement role hierarchy with inheritance
- Create delegation chains with expiration and constraints
- Build efficient path queries for authorization checks
- Add time-based constraints on delegations
- Implement audit trail for permission changes
- Create a visualization tool for the delegation hierarchy

**Expected Output**: A sophisticated permission system using Neo4j's graph capabilities for delegation chains.

## 3.4 Combined Queries

### 3.4.1 - REST API Using Both Postgres and Neo4j
**Objective**: Create an API that integrates relational and graph databases.

**Description**:
- Build an API that sources data from both PostgreSQL and Neo4j
- Create coordinated queries across both data stores
- Implement a unified data model that merges results
- Handle transaction management across databases
- Add error handling for multi-database operations
- Create performance optimizations for cross-database queries

**Expected Output**: A REST API that seamlessly integrates data from both relational and graph sources.

### 3.4.2 - Async Resolver Using Redis + SQL/Graph Combo
**Objective**: Create a high-performance data access layer with caching.

**Description**:
- Build an async resolver that coordinates SQL, Graph, and Redis
- Implement read-through caching for frequent queries
- Create cache invalidation strategies for writes
- Add TTL policies for different data types
- Implement batch operations across data stores
- Create monitoring for cache hit/miss rates

**Expected Output**: A high-performance data resolver with proper caching and multi-source capabilities.

### Branch Project 3.4: Cross-Store Resolver
**Objective**: Create a comprehensive API layer for accessing data across multiple storage types.

**Description**:
- Build a unified API for user profile data spanning multiple storage types
- Implement coordinated queries that combine SQL, Graph, and Cache data
- Create optimized data access paths based on query patterns
- Add caching strategies tailored to access patterns
- Implement proper transactional boundaries across stores
- Create a query planner that optimizes data retrieval
- Add monitoring and telemetry for cross-store operations

**Expected Output**: A sophisticated data access layer that transparently handles multi-store operations.

## Module 3 Capstone: School Directory API

**Objective**: Build a comprehensive school directory system that leverages both SQL and graph databases.

**Description**:
- Create a complete school directory API with users, roles, and organizational structure
- Implement SQL database for user profiles, courses, and standard relationships
- Use Neo4j for organizational hierarchy, permissions, and complex relationships
- Implement a caching layer for frequently accessed data
- Create proper schema migration patterns with Alembic
- Use transaction management across data stores
- Implement efficient query patterns for each storage type
- Add sophisticated permission delegation using graph relationships
- Create indexes and constraints for optimal performance
- Implement a unified API that abstracts the underlying storage details
- Add proper connection management and resource cleanup
- Create comprehensive error handling and recovery

**Expected Output**: A production-ready school directory API that demonstrates mastery of both SQL and graph database concepts.

**Success Criteria**:
- Efficient data retrieval across both SQL and graph databases
- Proper schema management with migrations
- Optimized query patterns for each database type
- Effective caching strategy
- Robust transaction handling
- Clean API abstraction over complex data sources
- Proper resource management and connection handling
