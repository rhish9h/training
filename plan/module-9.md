# 📘 Module 9: Deployment & DevOps

| Submodule            | Study | Project | Difficulty |
| -------------------- | ----- | ------- | ---------- |
| 9.1 Docker & Compose | 6h    | 3h      | I          |
| 9.2 CI/CD Pipelines  | 6h    | 3h      | I–A        |
| 9.3 Kubernetes Intro | 5h    | 3h      | A          |

### 9.1 Docker & Compose

| Item               | Description               | Learning Objectives                         | Micro-Project                                | Study | Build | Level |
| ------------------ | ------------------------- | ------------------------------------------- | -------------------------------------------- | ----- | ----- | ----- |
| 9.1.1 Dockerfile   | Containerize a Python app | - Create minimal, multi-stage builds        | Dockerfile for FastAPI service               | 2h    | 1h    | I     |
| 9.1.2 Compose Up   | Define local stacks       | - Orchestrate DB, cache, service in dev env | Compose file for blog API + Postgres + Redis | 2h    | 1h    | I     |
| 9.1.3 Healthchecks | Build resilient services  | - Add startup and readiness checks          | Healthcheck wrapper for all containers       | 2h    | 1h    | I     |

**Branch Project 9.1:** Local Dev Stack – One-command local environment using Docker Compose with app, DB, and cache.

### 9.2 CI/CD Pipelines

| Item                  | Description                 | Learning Objectives                           | Micro-Project                          | Study | Build | Level |
| --------------------- | --------------------------- | --------------------------------------------- | -------------------------------------- | ----- | ----- | ----- |
| 9.2.1 GitHub Actions  | Build-test pipeline         | - Auto-run test suites                        | Python CI for test + lint + type-check | 2h    | 1.5h  | I     |
| 9.2.2 Docker Publish  | Image registry integration  | - Push versioned builds to container registry | GH Action to push app to Docker Hub    | 2h    | 1h    | I     |
| 9.2.3 Deployment Step | Connect CI to prod/test env | - Deploy to test env with tag-based triggers  | GH CD deploy to Render/railway         | 2h    | 0.5h  | A     |

**Branch Project 9.2:** AutoShip – Full CI/CD pipeline for a Python service that runs tests, builds Docker image, and deploys on commit.

### 9.3 Kubernetes Intro

| Item                   | Description                    | Learning Objectives                 | Micro-Project                        | Study | Build | Level |
| ---------------------- | ------------------------------ | ----------------------------------- | ------------------------------------ | ----- | ----- | ----- |
| 9.3.1 Pods & Services  | Basics of K8s resource objects | - Define and expose services        | Deploy FastAPI app with LoadBalancer | 2h    | 1.5h  | A     |
| 9.3.2 Config & Secrets | Env vars, mounted secrets      | - Secure config with K8s constructs | Secret-injected DB credentials pod   | 1.5h  | 0.5h  | A     |
| 9.3.3 Autoscaling      | Resource scaling with HPA      | - Scale by CPU/memory metrics       | Enable HPA on high-CPU toy app       | 1.5h  | 1h    | A     |

**Branch Project 9.3:** Cluster Mini App – A three-tier app deployed to local K8s cluster with scaling and secret management.

**Capstone 9:** DevOps Pipeline Toolkit – Dockerized, CI/CD-deployed FastAPI microservice with optional K8s deployment and autoscaling using GitHub Actions.
