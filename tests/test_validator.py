from validator import validate_metrics


def test_validate_metrics_success():
    metrics = {
        "cpu_usage_percent": 45,
        "memory_usage_percent": 60,
        "disk_usage_percent": 70,
        "service_status": "healthy",
        "latency_ms": 150
    }
    assert validate_metrics(metrics) == []


def test_validate_metrics_failure():
    metrics = {
        "cpu_usage_percent": 95,
        "memory_usage_percent": 92,
        "disk_usage_percent": 97,
        "service_status": "down",
        "latency_ms": 350
    }
    errors = validate_metrics(metrics)
    assert len(errors) == 5