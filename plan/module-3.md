# 📘 Module 3: Data Persistence – SQL + Graph

| Submodule                | Study | Project | Difficulty |
| ------------------------ | ----- | ------- | ---------- |
| 3.1 Async SQLAlchemy     | 8h    | 4h      | I          |
| 3.2 Alembic & Migrations | 4h    | 3h      | I          |
| 3.3 Neo4j & Cypher       | 6h    | 4h      | A          |
| 3.4 Combined Queries     | 4h    | 3h      | A          |

### 3.1 Async SQLAlchemy

| Item                | Description                   | Learning Objectives                         | Micro-Project                | Study | Build | Level |
| ------------------- | ----------------------------- | ------------------------------------------- | ---------------------------- | ----- | ----- | ----- |
| 3.1.1 ORM Basics    | Define tables, async sessions | - Create models, manage sessions            | CRUD for Bookstore app       | 3h    | 2h    | I     |
| 3.1.2 Eager Loading | Improve query performance     | - Use selectinload/joinedload appropriately | Author-Book relationship API | 2h    | 1h    | I     |
| 3.1.3 Transactions  | Safe state changes            | - Handle rollbacks, nesting, atomic ops     | Order checkout workflow      | 3h    | 1h    | I     |

**Branch Project 3.1:** Library DB API – Book + Author + Category relations with selectinload and transactions.

### 3.2 Alembic & Migrations

| Item                | Description              | Learning Objectives                 | Micro-Project                   | Study | Build | Level |
| ------------------- | ------------------------ | ----------------------------------- | ------------------------------- | ----- | ----- | ----- |
| 3.2.1 Versioned DDL | Schema migrations        | - Init migrations, create revisions | Version-controlled movie schema | 2h    | 1.5h  | I     |
| 3.2.2 Autogenerate  | Generate from model diff | - Use Alembic CLI for diffs         | Update schema with added fields | 2h    | 1.5h  | I     |

**Branch Project 3.2:** Blog Schema History – DB schema with 3 evolution steps and migration control.

### 3.3 Neo4j & Cypher

| Item                 | Description              | Learning Objectives                | Micro-Project                       | Study | Build | Level |
| -------------------- | ------------------------ | ---------------------------------- | ----------------------------------- | ----- | ----- | ----- |
| 3.3.1 Graph Basics   | Nodes, edges, labels     | - Create users, roles, permissions | Simple org chart graph              | 2h    | 1.5h  | A     |
| 3.3.2 Cypher Queries | Pattern matching         | - Query relationships and paths    | Shortest path for delegation chains | 2h    | 1.5h  | A     |
| 3.3.3 Constraints    | Graph schema enforcement | - Use uniqueness constraints       | Clean graph with safe merges        | 2h    | 1h    | A     |

**Branch Project 3.3:** Delegation Resolver – Build and query user permission delegation in Neo4j.

### 3.4 Combined Queries

| Item               | Description                  | Learning Objectives                  | Micro-Project                                | Study | Build | Level |
| ------------------ | ---------------------------- | ------------------------------------ | -------------------------------------------- | ----- | ----- | ----- |
| 3.4.1 Polyglot API | Join SQL + Graph results     | - Aggregate across storage types     | REST API using both Postgres and Neo4j       | 2h    | 1.5h  | A     |
| 3.4.2 Cache Layer  | Read-through for performance | - Implement multi-source data access | Async resolver using Redis + SQL/Graph combo | 2h    | 1.5h  | A     |

**Branch Project 3.4:** Cross-Store Resolver – API layer combining SQL, graph, and cache for user profile views.

**Capstone 3:** School Directory API – A hybrid API that manages users, roles, and org charts using both SQL and Neo4j, complete with migrations, indexes, and a cache layer.
