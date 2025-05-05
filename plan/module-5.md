# 📘 Module 5: Redis & Caching Strategies

| Submodule               | Study | Project | Difficulty |
| ----------------------- | ----- | ------- | ---------- |
| 5.1 Redis Core Concepts | 5h    | 3h      | I          |
| 5.2 Advanced Caching    | 5h    | 3h      | I–A        |
| 5.3 Rate Limiting & TTL | 4h    | 3h      | A          |

### 5.1 Redis Core Concepts

| Item                  | Description                  | Learning Objectives           | Micro-Project                         | Study | Build | Level |
| --------------------- | ---------------------------- | ----------------------------- | ------------------------------------- | ----- | ----- | ----- |
| 5.1.1 Data Structures | Strings, hashes, lists, sets | - Use Redis types effectively | Redis-powered leaderboard tracker     | 2h    | 1.5h  | I     |
| 5.1.2 Pub/Sub         | Publish/Subscribe model      | - Build messaging channels    | Simple chatroom with Redis pub/sub    | 2h    | 1.5h  | I     |
| 5.1.3 Redis CLI       | Local exploration/debugging  | - Monitor keys, TTLs          | CLI scripts to inspect Redis instance | 1h    | 0.5h  | I     |

**Branch Project 5.1:** Leaderboard API – An API using Redis sorted sets to maintain and query a live leaderboard.

### 5.2 Advanced Caching

| Item                   | Description                    | Learning Objectives                  | Micro-Project                         | Study | Build | Level |
| ---------------------- | ------------------------------ | ------------------------------------ | ------------------------------------- | ----- | ----- | ----- |
| 5.2.1 Cache Decorators | Wrap functions for memoization | - Cache expensive function calls     | LRU + Redis decorator for weather API | 2h    | 1.5h  | I     |
| 5.2.2 Read-Through     | Abstract data fetch + caching  | - Serve cache-first, fallback to DB  | Article content cache                 | 2h    | 1.5h  | I     |
| 5.2.3 Write Strategies | Invalidation and consistency   | - Write-through and TTL invalidation | Comment cache with TTL update trigger | 1h    | 1h    | A     |

**Branch Project 5.2:** Smart Cache API – Layered cache abstraction with decorator-based control and TTL policies.

### 5.3 Rate Limiting & TTL

| Item                  | Description                   | Learning Objectives                      | Micro-Project                             | Study | Build | Level |
| --------------------- | ----------------------------- | ---------------------------------------- | ----------------------------------------- | ----- | ----- | ----- |
| 5.3.1 Token Bucket    | Redis + Lua based limiter     | - Build scalable per-user rate limiting  | Token bucket limiter middleware           | 2h    | 1.5h  | A     |
| 5.3.2 Session Expiry  | TTL for access/session tokens | - Auto-expire keys for inactive sessions | JWT store with auto expiration            | 1h    | 1h    | A     |
| 5.3.3 Circuit Breaker | Redis as state tracker        | - Track retries/failures in Redis        | Circuit breaker cache for remote services | 1h    | 0.5h  | A     |

**Branch Project 5.3:** Policy Limiter – Rate-limited API gateway using token bucket algorithm and cache-based circuit breaker.

**Capstone 5:** Book Review Caching Layer – REST API using Redis for session management, read-through caching, live rate limiting, and circuit breaker pattern.
