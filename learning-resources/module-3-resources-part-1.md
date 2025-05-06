# Module 3: Data Persistence – SQL + Graph - Learning Resources

## 3.1 Async SQLAlchemy

### 3.1.1 - ORM Basics

#### Core Concepts
- Async SQLAlchemy 2.0 fundamentals
- ORM model definition and relationships
- Async session management
- CRUD operations with SQLAlchemy async
- Connection lifecycle management
- PostgreSQL integration

#### Search Terms
- "SQLAlchemy 2.0 async tutorial"
- "Async ORM Python SQLAlchemy"
- "SQLAlchemy model definition best practices"
- "Async session management SQLAlchemy"
- "SQLAlchemy relationship definitions"
- "PostgreSQL SQLAlchemy async setup"

#### Suggested Learning Path
1. **SQLAlchemy 2.0 Fundamentals** (1-2 hours)
   - Learn SQLAlchemy 2.0 architecture
   - Understand ORM vs. Core approaches
   - Set up SQLAlchemy in an async project

2. **Model Definition** (1 hour)
   - Create SQLAlchemy models and tables
   - Define column types and constraints
   - Implement model relationships

3. **Async Session Management** (1-2 hours)
   - Understand session lifecycle
   - Create session factories and dependencies
   - Implement proper connection handling

4. **CRUD Operations** (1 hour)
   - Implement create, read, update, delete
   - Learn querying patterns
   - Use native PostgreSQL features

5. **Integration with Web Framework** (1 hour)
   - Connect SQLAlchemy with FastAPI
   - Create database dependencies
   - Implement proper error handling

#### Recommended Resources

**Official Documentation**
- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/)
- [SQLAlchemy 2.0 ORM Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- [SQLAlchemy Async Extension](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

**Articles & Tutorials**
- [FastAPI with Async SQLAlchemy 2.0](https://medium.com/@tclaitken/setting-up-a-fastapi-app-with-async-sqlalchemy-2-0-pydantic-v2-e6c540be4308)
- [SQLAlchemy 2.0 - What's New](https://www.sqlalchemy.org/blog/2022/06/14/sqlalchemy-2.0.0b1-released/)
- [Using SQLAlchemy 2.0 with AsyncIO](https://dev.to/obisk/using-sqlalchemy-2-async-a-tutorial-58db)

**YouTube Videos**
- [SQLAlchemy 2.0 - New Features (Michael Kennedy)](https://www.youtube.com/watch?v=r6vkQ7XQtk0)
- [FastAPI with Async SQLAlchemy (Patrick Loeber)](https://www.youtube.com/watch?v=2g1ZjN1NCmM)
- [Modern SQLAlchemy (PyConUS 2023)](https://www.youtube.com/watch?v=XWLo5_Cz-C0)

**GitHub Repositories**
- [sqlalchemy/sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) - Official repository
- [tiangolo/sqlmodel](https://github.com/tiangolo/sqlmodel) - SQLModel (built on SQLAlchemy)
- [fastapi-sqlalchemy-example](https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/backend/app/app/db)

---

### 3.1.2 - Eager Loading

#### Core Concepts
- Relationship loading strategies
- Selectinload vs. joinedload performance
- N+1 query problem and solutions
- Query optimization techniques
- Relationship configuration best practices
- Author-book relationship patterns

#### Search Terms
- "SQLAlchemy eager loading strategies"
- "Selectinload vs joinedload performance"
- "SQLAlchemy N+1 query problem"
- "Optimize relationship loading SQLAlchemy"
- "SQLAlchemy relationship lazy loading"
- "SQLAlchemy async relationship loading"

#### Suggested Learning Path
1. **Relationship Loading Fundamentals** (1 hour)
   - Understand lazy loading vs. eager loading
   - Learn about N+1 query problems
   - Explore different loading strategies

2. **Selectinload Strategy** (1 hour)
   - Understand selectinload mechanics
   - Learn best use cases
   - Implement and test performance

3. **Joinedload Strategy** (1 hour)
   - Understand joinedload mechanics
   - Learn best use cases
   - Implement and test performance

4. **Comparative Analysis** (1 hour)
   - Benchmark different loading strategies
   - Analyze query execution plans
   - Optimize based on access patterns

5. **Integration in Applications** (1 hour)
   - Implement in real-world scenarios
   - Create reusable loading patterns
   - Monitor and profile performance

#### Recommended Resources

**Official Documentation**
- [SQLAlchemy Relationship Loading](https://docs.sqlalchemy.org/en/20/orm/loading_relationships.html)
- [SQLAlchemy Loading Reference](https://docs.sqlalchemy.org/en/20/orm/loading_references.html)
- [SQLAlchemy Eager Loading](https://docs.sqlalchemy.org/en/20/orm/tutorial.html#eager-loading)

**Articles & Tutorials**
- [Eager Loading vs Lazy Loading in SQLAlchemy ORM](https://pythonfriday.dev/2021/08/85-eager-loading-vs-lazy-loading-in-sqlalchemy-orm/)
- [SQLAlchemy: Relationship Loading Techniques](https://dev.to/curiousdev/sqlalchemy-relationship-loading-techniques-4m10)
- [SQLAlchemy Performance Optimization](https://medium.com/@khrisrichardson/sqlalchemy-performance-optimization-using-eager-loading-9e5d76844ef1)

**YouTube Videos**
- [SQLAlchemy ORM Relationships (Pretty Printed)](https://www.youtube.com/watch?v=UEY5mpu4Fig)
- [SQLAlchemy Performance Optimization (PyConUS 2022)](https://www.youtube.com/watch?v=N5g0D7BqWRo)
- [SQLAlchemy Deep Dive (ArjanCodes)](https://www.youtube.com/watch?v=tHfHzBhX8JY)

**GitHub Repositories**
- [sqlalchemy-orm-patterns](https://github.com/sqlalchemy/sqlalchemy/tree/main/examples)
- [sqlalchemy-benchmarks](https://github.com/zzzeek/sqlalchemy/tree/master/examples/performance)

---

### 3.1.3 - Transactions

#### Core Concepts
- Transaction management in SQLAlchemy
- ACID properties in database transactions
- Nested transactions and savepoints
- Error handling and rollbacks
- Atomic operations guarantees
- Transaction isolation levels

#### Search Terms
- "SQLAlchemy async transaction management"
- "Nested transactions SQLAlchemy"
- "Database ACID properties Python"
- "Transaction rollback SQLAlchemy async"
- "Savepoints in SQLAlchemy transactions"
- "SQLAlchemy transaction isolation levels"

#### Suggested Learning Path
1. **Transaction Fundamentals** (1 hour)
   - Understand ACID properties
   - Learn SQLAlchemy transaction API
   - Explore transaction contexts

2. **Async Transaction Management** (1-2 hours)
   - Implement async transaction patterns
   - Learn proper error handling
   - Create transaction decorators

3. **Nested Transactions** (1 hour)
   - Understand nested transaction mechanics
   - Implement subtransactions
   - Learn savepoint usage

4. **Rollback Scenarios** (1 hour)
   - Implement error handling with rollbacks
   - Create retry logic
   - Design fault-tolerant operations

5. **Advanced Transaction Control** (1 hour)
   - Configure isolation levels
   - Implement connection pooling strategies
   - Create transaction monitoring

#### Recommended Resources

**Official Documentation**
- [SQLAlchemy Transactions](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html)
- [SQLAlchemy AsyncSession](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#sqlalchemy.ext.asyncio.AsyncSession)
- [SQLAlchemy Nested Transactions](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html#nested-transactions)

**Articles & Tutorials**
- [SQLAlchemy Transaction Management](https://medium.com/@johndcobb/transaction-management-in-sqlalchemy-5b8294a8964)
- [Async Transactions with SQLAlchemy](https://dev.to/fanimokhtar/managing-transactions-in-fastapi-with-sqlalchemy-2n28)
- [Understanding Database Transactions in Python](https://medium.com/@alexandre.laplante/database-transactions-in-python-with-sqlalchemy-ef7c8c764a9e)

**YouTube Videos**
- [SQLAlchemy Transaction Management (Patrick Loeber)](https://www.youtube.com/watch?v=2g1ZjN1NCmM)
- [Database Transactions Explained (ArjanCodes)](https://www.youtube.com/watch?v=AzBCUf0Ej1c)
- [SQLAlchemy Session Management (PyConUS 2021)](https://www.youtube.com/watch?v=prO1c_Wq8YM)

**GitHub Repositories**
- [sqlalchemy-transaction-examples](https://github.com/sqlalchemy/sqlalchemy/tree/main/examples/transaction)
- [fastapi-sqlalchemy-transaction](https://github.com/tiangolo/full-stack-fastapi-postgresql/blob/master/backend/app/app/db/base.py)

---

### Branch Project 3.1: Library DB API

#### Core Concepts
- Complex relationship modeling
- Advanced query optimization
- Transaction management for multi-step operations
- Connection pooling strategies
- Data access layer architecture
- API integration patterns

#### Search Terms
- "SQLAlchemy complex relationship modeling"
- "Library database schema design"
- "Data access layer patterns Python"
- "SQLAlchemy connection pooling optimization"
- "Transaction management multi-step operations"
- "SQLAlchemy advanced query techniques"

#### Suggested Learning Path
1. **Database Schema Design** (1-2 hours)
   - Design library domain model
   - Create entity relationships
   - Plan query access patterns

2. **Data Access Layer Architecture** (1-2 hours)
   - Implement repository pattern
   - Create service abstractions
   - Design API integration

3. **Optimization Techniques** (1-2 hours)
   - Implement query optimization
   - Configure connection pooling
   - Create caching strategies

4. **Transaction Management** (1-2 hours)
   - Design multi-step operations
   - Implement proper error handling
   - Create atomic operations

5. **API Exposure** (1 hour)
   - Design REST endpoints
   - Create serialization/deserialization
   - Implement filtering and pagination

#### Recommended Resources

**Official Documentation**
- [SQLAlchemy ORM Cookbook](https://github.com/zzzeek/sqlalchemy_cookbook)
- [SQLAlchemy Performance Optimization](https://docs.sqlalchemy.org/en/20/faq/performance.html)
- [SQLAlchemy Connection Pooling](https://docs.sqlalchemy.org/en/20/core/pooling.html)

**Articles & Tutorials**
- [Building a Data Access Layer with SQLAlchemy](https://medium.com/analytics-vidhya/building-a-data-access-layer-with-sqlalchemy-abb77579cd1b)
- [Database Design Patterns for Library Management](https://dev.to/ovid/database-design-patterns-for-library-management-52ki)
- [Optimizing SQLAlchemy for Production](https://medium.com/@matthewdavidroddy/10-ways-to-improve-sqlalchemy-performance-3241063e3cdb)

**YouTube Videos**
- [SQLAlchemy Best Practices (PyConUS 2022)](https://www.youtube.com/watch?v=0PSdzUxRYpA)
- [Database Architecture Patterns (ArjanCodes)](https://www.youtube.com/watch?v=5G_Gl_izL0w)
- [Library Database Design (Tech With Tim)](https://www.youtube.com/watch?v=SPPTQwU0FTo)

**GitHub Repositories**
- [library-management-system](https://github.com/aditya-2403/library-management-system) - Example project
- [sqlalchemy-best-practices](https://github.com/zzzeek/sqlalchemy_cookbook/tree/master/examples)

## 3.2 Alembic & Migrations

### 3.2.1 - Versioned DDL

#### Core Concepts
- Database schema migration fundamentals
- Alembic setup and configuration
- Migration script creation and structure
- Upgrade and downgrade operations
- Migration versioning and branching
- Database version control workflow

#### Search Terms
- "Alembic SQLAlchemy migration tutorial"
- "Database schema versioning best practices"
- "Alembic revision creation guide"
- "Upgrade downgrade migrations Alembic"
- "SQLAlchemy Alembic integration setup"
- "Database version control workflow"

#### Suggested Learning Path
1. **Migration Fundamentals** (1 hour)
   - Understand schema evolution challenges
   - Learn database migration concepts
   - Explore version control for databases

2. **Alembic Setup** (1 hour)
   - Initialize Alembic in a project
   - Configure database connection
   - Create baseline migration

3. **Creating Migrations** (1 hour)
   - Generate manual migration scripts
   - Learn migration script structure
   - Implement schema changes

4. **Upgrade/Downgrade Operations** (1 hour)
   - Design reversible migrations
   - Implement upgrade logic
   - Create downgrade operations

5. **Migration Management** (1 hour)
   - Manage migration branches
   - Handle migration dependencies
   - Implement migration testing

#### Recommended Resources

**Official Documentation**
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [Alembic Migration Operations](https://alembic.sqlalchemy.org/en/latest/ops.html)

**Articles & Tutorials**
- [Database Migrations with Alembic](https://testdriven.io/blog/database-migrations-with-alembic/)
- [Managing Database Migrations with Alembic](https://medium.com/analytics-vidhya/alembic-database-migration-management-e21ebf46e42a)
- [Alembic: Python's Database Migration Tool](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

**YouTube Videos**
- [Database Migrations with Alembic (Patrick Loeber)](https://www.youtube.com/watch?v=SdcH6IEi6nE)
- [Alembic Database Migrations Tutorial (Pretty Printed)](https://www.youtube.com/watch?v=nt5sSr1A_qw)
- [SQLAlchemy and Alembic (PyConUS 2022)](https://www.youtube.com/watch?v=Zx09Lp43Rfw)

**GitHub Repositories**
- [zzzeek/alembic](https://github.com/sqlalchemy/alembic) - Official repository
- [alembic-examples](https://github.com/sqlalchemy/alembic/tree/main/docs/build/tutorial)

---

### 3.2.2 - Autogenerate

#### Core Concepts
- Alembic autogeneration capabilities
- Model to migration workflow
- Detecting schema differences
- Migration customization
- Data migrations alongside schema changes
- Testing migration reversibility

#### Search Terms
- "Alembic autogenerate migrations tutorial"
- "SQLAlchemy model to migration workflow"
- "Alembic detect schema differences"
- "Customize Alembic autogenerated migrations"
- "Data migration alongside schema changes"
- "Testing Alembic migration reversibility"

#### Suggested Learning Path
1. **Autogeneration Basics** (1 hour)
   - Understand autogeneration mechanics
   - Configure metadata comparison
   - Create first autogenerated migration

2. **Model-Driven Migrations** (1 hour)
   - Implement model changes
   - Generate migrations from models
   - Review autogenerated code

3. **Customizing Migrations** (1 hour)
   - Modify autogenerated migrations
   - Add custom operations
   - Implement template customization

4. **Data Migrations** (1 hour)
   - Combine schema and data changes
   - Implement data transformation
   - Create data backfill operations

5. **Testing & Validation** (1 hour)
   - Test migration application
   - Verify migration reversibility
   - Implement CI for migrations

#### Recommended Resources

**Official Documentation**
- [Alembic Auto Generate](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
- [Alembic Customizing Templates](https://alembic.sqlalchemy.org/en/latest/cookbook.html#customizing-revision-message-templates)
- [Alembic Batch Operations](https://alembic.sqlalchemy.org/en/latest/batch.html)

**Articles & Tutorials**
- [SQLAlchemy Models to Alembic Migrations](https://medium.com/@philipkogel/make-alembic-migrations-work-with-sqlalchemy-models-81db733b3609)
- [Handling Data Migrations with Alembic](https://testdriven.io/blog/migrating-data-with-alembic/)
- [Customizing Alembic Autogenerate](https://medium.com/@amir_masoud/a-few-alembic-tricks-i-learned-the-hard-way-e7d2941dbb13)

**YouTube Videos**
- [Alembic Autogeneration Deep Dive (PyConUS 2023)](https://www.youtube.com/watch?v=9jGJhMpfNLY)
- [SQLAlchemy Models to Migrations (ArjanCodes)](https://www.youtube.com/watch?v=dDyF9TwsKw0)
- [Advanced Alembic Usage (PyTexas 2022)](https://www.youtube.com/watch?v=CyCNtIZXBTE)

**GitHub Repositories**
- [alembic-examples](https://github.com/sqlalchemy/alembic/tree/main/examples)
- [alembic-autogenerate-example](https://github.com/sqlalchemy/alembic/tree/main/docs/build/autogenerate)

---

### Branch Project 3.2: Blog Schema History

#### Core Concepts
- Comprehensive database evolution strategy
- Migration dependency management
- Multi-phase schema evolution
- Data migration techniques
- Version checking in applications
- Migration documentation best practices

#### Search Terms
- "Database schema evolution strategy"
- "Multi-phase migration planning"
- "Alembic migration dependencies"
- "Data migration large tables"
- "Version checking database applications"
- "Database migration documentation best practices"

#### Suggested Learning Path
1. **Schema Evolution Planning** (1-2 hours)
   - Design three evolution phases
   - Plan migration dependencies
   - Create migration roadmap

2. **Implementation Strategy** (1-2 hours)
   - Implement initial schema
   - Create phased migration scripts
   - Design testing approach

3. **Data Migration** (1-2 hours)
   - Implement data transformation
   - Create backfill operations
   - Design rollback strategies

4. **Application Integration** (1 hour)
   - Implement version checking
   - Create migration-aware code
   - Design schema compatibility

5. **Documentation & Management** (1 hour)
   - Create migration documentation
   - Design version control workflow
   - Implement CI/CD for migrations

#### Recommended Resources

**Official Documentation**
- [Alembic Branches](https://alembic.sqlalchemy.org/en/latest/branches.html)
- [Alembic Data Migrations](https://alembic.sqlalchemy.org/en/latest/cookbook.html#data-migrations)
- [Alembic Command-Line Interface](https://alembic.sqlalchemy.org/en/latest/api/commands.html)

**Articles & Tutorials**
- [Managing Database Schema Evolution](https://medium.com/engineering-at-birdie/managing-your-database-schema-migrations-with-alembic-and-sqlalchemy-part-1-e88c4262e1c)
- [Zero Downtime Database Migrations](https://medium.com/gusto-engineering/zero-downtime-schema-migrations-with-laravel-b9738320d2ab)
- [Documenting Database Migrations](https://dev.to/rhymes/better-schema-migrations-in-your-projects-2n9j)

**YouTube Videos**
- [Database Schema Evolution Patterns (PyConUS 2021)](https://www.youtube.com/watch?v=A0V8cOJ9lD8)
- [Zero Downtime Migrations (PyCon Sweden)](https://www.youtube.com/watch?v=A0V8cOJ9lD8)
- [Managing Complex DB Changes (DBCEU 2023)](https://www.youtube.com/watch?v=qfgL1lXaIE0)

**GitHub Repositories**
- [alembic-multidb-example](https://github.com/sqlalchemy/alembic/tree/main/examples/multidb)
- [zero-downtime-migrations](https://github.com/tbicr/django-pg-zero-downtime-migrations)
