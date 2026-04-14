# Platform Test Automation

A lightweight Python-based validation tool designed to simulate platform health checks and automated testing workflows used in systems engineering.

## Overview
This project validates key system metrics such as CPU usage, memory utilization, disk usage, service health, and latency to ensure platform stability and reliability.

## Features
- Automated validation of system health metrics
- Structured logging for observability and debugging
- Unit tests for validation logic using pytest
- Modular and extensible design for additional checks

## Tech Stack
- Python
- Pytest
- JSON
- Logging

## Project Structure
```text
platform-test-automation/
├── validator.py
├── sample_metrics.json
├── bad_metrics.json
├── requirements.txt
├── .gitignore
├── README.md
└── tests/
    └── test_validator.py
