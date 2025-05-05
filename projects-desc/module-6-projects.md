# Module 6: Observability & Monitoring - Project Descriptions

## 6.1 Metrics & Prometheus

### 6.1.1 - Prometheus Metrics FastAPI Endpoint
**Objective**: Implement custom metrics collection in a FastAPI application.

**Description**:
- Set up a Prometheus client in a FastAPI application
- Create custom metrics for different measurement types
- Implement counters for request tracking
- Add histograms for response time measurements
- Create gauges for resource utilization
- Implement a metrics endpoint for scraping
- Add labels for request segmentation (endpoint, status, method)
- Create middleware for automatic request instrumentation

**Expected Output**: A FastAPI application with a /metrics endpoint exposing custom application metrics.

### 6.1.2 - Service Dashboard with 3 Metrics
**Objective**: Create a Grafana dashboard for visualizing service metrics.

**Description**:
- Set up Grafana with Prometheus data source
- Create a dashboard with three key metrics panels
- Implement a request rate panel with proper time range
- Add a latency histogram panel with percentiles
- Create an error rate panel with thresholds
- Add variables for filtering by service/endpoint
- Implement annotations for deployment events
- Create a cohesive layout with proper organization

**Expected Output**: A Grafana dashboard that visualizes key service metrics from Prometheus.

### 6.1.3 - CLI Script Reporting to Pushgateway
**Objective**: Collect metrics from batch processes using Prometheus Pushgateway.

**Description**:
- Set up Prometheus Pushgateway for metrics collection
- Create a CLI script that performs a batch operation
- Implement metrics collection during processing
- Add job and instance labels for identification
- Push metrics to Pushgateway upon completion
- Create metrics for duration, success/failure counts
- Implement error handling for failed metric pushes

**Expected Output**: A CLI tool that reports its execution metrics to Prometheus Pushgateway.

### Branch Project 6.1: Metrics Service
**Objective**: Build a comprehensive metrics collection system for a high-traffic API.

**Description**:
- Create a high-throughput API with comprehensive instrumentation
- Implement RED metrics (Rate, Errors, Duration)
- Add custom business metrics for key operations
- Create resource utilization metrics (CPU, memory, connections)
- Implement a Prometheus exporter with efficient collection
- Add middleware for automatic request instrumentation
- Create detailed Grafana dashboards with multiple panels
- Implement alerting based on threshold violations
- Add job-specific metrics for background processes
- Create Pushgateway integration for batch operations

**Expected Output**: A fully instrumented service with comprehensive metrics and dashboards.

## 6.2 Distributed Tracing

### 6.2.1 - Correlated Trace ID Across Service Calls
**Objective**: Implement basic distributed tracing with manual context propagation.

**Description**:
- Create a multi-service application with dependencies
- Implement trace ID generation at entry points
- Add trace context propagation between services
- Create middleware for capturing trace information
- Implement logging with trace ID correlation
- Add request headers for context propagation
- Create a simple trace viewer for connected logs

**Expected Output**: A system that propagates trace IDs across service boundaries for request correlation.

### 6.2.2 - Traced REST API with Latency Visualization
**Objective**: Implement OpenTelemetry instrumentation for a REST API.

**Description**:
- Set up OpenTelemetry SDK in a REST API
- Create spans for key operations and requests
- Add attributes for request details and parameters
- Implement nested spans for database and external calls
- Create custom span events for important operations
- Add proper error handling in spans
- Implement an exporter for trace data
- Create visualization for service latency breakdown

**Expected Output**: A REST API with comprehensive OpenTelemetry instrumentation and latency visualization.

### 6.2.3 - Trace Flow Across Multi-Service Stack
**Objective**: Set up a complete distributed tracing system with Jaeger.

**Description**:
- Set up Jaeger with Docker for trace collection
- Configure OpenTelemetry collector for trace processing
- Create a multi-service application with trace instrumentation
- Implement proper context propagation between services
- Add sampling strategies for high-volume environments
- Create custom span processors for data enrichment
- Implement a Jaeger UI for trace visualization and exploration

**Expected Output**: A complete distributed tracing system with Jaeger for a multi-service application.

### Branch Project 6.2: Instrumented Search Service
**Objective**: Build a fully traced search service with detailed latency analysis.

**Description**:
- Create a search API with multiple backend data sources
- Implement comprehensive OpenTelemetry instrumentation
- Add spans for each component in the search pipeline
- Create detailed attributes for query parameters and results
- Implement proper context propagation across components
- Add custom metrics derived from trace data
- Create Jaeger integration for trace visualization
- Implement latency breakdown dashboards
- Add performance bottleneck identification
- Create correlation between traces and logs

**Expected Output**: A fully instrumented search service with detailed latency analysis and visualization.

## 6.3 Structured Logging & Loki

### 6.3.1 - JSON Logs with Labels and Correlation ID
**Objective**: Implement structured logging with proper correlation.

**Description**:
- Set up JSON-formatted structured logging
- Implement correlation ID generation and propagation
- Add standard fields for all log entries
- Create context-specific labels for filtering
- Implement request/response logging with proper formatting
- Add service and environment labels
- Create logging middleware for web frameworks

**Expected Output**: A logging system that produces structured JSON logs with correlation IDs and labels.

### 6.3.2 - Grafana-Connected Loki Logs Panel
**Objective**: Set up centralized log collection and visualization with Loki.

**Description**:
- Set up Loki for log ingestion and storage
- Configure log shipping from application to Loki
- Create a Grafana dashboard with log panels
- Implement LogQL queries for log filtering
- Add derived fields for clickable links
- Create log volume visualization
- Implement log label selection via dashboard variables

**Expected Output**: A Grafana dashboard with Loki-based log panels and filtering capabilities.

### 6.3.3 - Custom Logger with Alert-Ready Format
**Objective**: Create a sophisticated logging system with alerting capabilities.

**Description**:
- Implement a custom logger with alert-ready formatting
- Add log levels with proper threshold configuration
- Create alert triggers based on log patterns
- Implement rate-based alerting for error conditions
- Add context-aware log enrichment
- Create alert notifications via multiple channels
- Implement alert grouping and deduplication

**Expected Output**: A custom logging system with built-in alerting capabilities.

### Branch Project 6.3: Unified Log Pipeline
**Objective**: Create a comprehensive logging infrastructure with visualization and analysis.

**Description**:
- Build a complete logging pipeline with multiple service sources
- Implement structured JSON logging across all services
- Create correlation between logs, traces, and metrics
- Add Loki for centralized log collection and indexing
- Implement log parsing and field extraction
- Create Grafana dashboards for log visualization and exploration
- Add log-based alerting for critical conditions
- Implement log retention and archiving policies
- Create role-based access controls for logs
- Add sophisticated LogQL queries for log analysis

**Expected Output**: A unified logging infrastructure with collection, visualization, and analysis capabilities.

## Module 6 Capstone: Weather API Monitoring Suite

**Objective**: Build a comprehensive observability solution for a weather API service.

**Description**:
- Create a weather API service with multiple data sources
- Implement comprehensive metrics collection with Prometheus
- Add detailed tracing with OpenTelemetry for request flow analysis
- Create structured logging with correlation across components
- Implement Loki for centralized log collection and analysis
- Add Jaeger for distributed trace visualization
- Create Grafana dashboards for unified monitoring
- Implement alerts for SLO violations and critical conditions
- Add custom instrumentation for business-specific metrics
- Create synthetic monitors for API health checks
- Implement performance analysis and bottleneck identification
- Add user experience metrics and analytics

**Expected Output**: A fully observable weather API with integrated metrics, traces, and logs.

**Success Criteria**:
- Complete visibility into system performance and health
- Correlated observability data across metrics, traces, and logs
- Effective alerting for critical conditions
- Detailed latency breakdown for performance analysis
- Comprehensive dashboards for monitoring and troubleshooting
- Proper instrumentation across all service components
- Quick identification of issues and root causes
