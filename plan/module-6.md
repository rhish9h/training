# 📘 Module 6: Observability & Monitoring

| Submodule                     | Study | Project | Difficulty |
| ----------------------------- | ----- | ------- | ---------- |
| 6.1 Metrics & Prometheus      | 5h    | 3h      | I          |
| 6.2 Distributed Tracing       | 5h    | 3h      | A          |
| 6.3 Structured Logging & Loki | 5h    | 2h      | I–A        |

### 6.1 Metrics & Prometheus

| Item                      | Description                  | Learning Objectives                      | Micro-Project                       | Study | Build | Level |
| ------------------------- | ---------------------------- | ---------------------------------------- | ----------------------------------- | ----- | ----- | ----- |
| 6.1.1 Prometheus Exporter | Expose custom metrics        | - Track HTTP duration, errors, app stats | Prometheus metrics FastAPI endpoint | 2h    | 1.5h  | I     |
| 6.1.2 Grafana Dashboard   | Visualize app behavior       | - Build panels for counters, histograms  | Service dashboard with 3 metrics    | 2h    | 1h    | I     |
| 6.1.3 Pushgateway         | Export from short-lived jobs | - Capture metrics from CLI/batch tools   | CLI script reporting to Pushgateway | 1h    | 0.5h  | I     |

**Branch Project 6.1:** Metrics Service – Live metrics dashboard for a request-intensive API using Prometheus + Grafana.

### 6.2 Distributed Tracing

| Item                 | Description                    | Learning Objectives                            | Micro-Project                              | Study | Build | Level |
| -------------------- | ------------------------------ | ---------------------------------------------- | ------------------------------------------ | ----- | ----- | ----- |
| 6.2.1 Trace Contexts | Propagate request context      | - Use trace IDs and spans                      | Correlated trace ID across service calls   | 2h    | 1.5h  | A     |
| 6.2.2 OpenTelemetry  | End-to-end distributed tracing | - Use OTEL SDK, exporters, span linking        | Traced REST API with latency visualization | 2h    | 1.5h  | A     |
| 6.2.3 Jaeger Setup   | Visualize traces               | - Deploy Jaeger with Docker and OTEL collector | Trace flow across multi-service stack      | 1h    | 1h    | A     |

**Branch Project 6.2:** Instrumented Search Service – Fully traced FastAPI search API showing latency breakdowns.

### 6.3 Structured Logging & Loki

| Item                      | Description                     | Learning Objectives               | Micro-Project                            | Study | Build | Level |
| ------------------------- | ------------------------------- | --------------------------------- | ---------------------------------------- | ----- | ----- | ----- |
| 6.3.1 JSON Logging        | Log in machine-parsable formats | - Filterable structured fields    | JSON logs with labels and correlation ID | 2h    | 1h    | I     |
| 6.3.2 Loki + Grafana      | Centralized logging             | - Query logs using Grafana        | Grafana-connected Loki logs panel        | 2h    | 1h    | I     |
| 6.3.3 Log Levels & Alerts | Logging best practices          | - Separate levels, trigger alerts | Custom logger with alert-ready format    | 1h    | 0.5h  | A     |

**Branch Project 6.3:** Unified Log Pipeline – Multi-level JSON logger connected to Loki with filters and Grafana UI.

**Capstone 6:** Weather API Monitoring Suite – End-to-end observability stack (Prometheus + Grafana + Loki + OTEL) on a real-world REST API with tracing, alerts, and visualization.
