import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


def load_metrics(file_path: str) -> Dict[str, Any]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Metrics file not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_metrics(metrics: Dict[str, Any]) -> List[str]:
    errors: List[str] = []

    cpu = metrics.get("cpu_usage_percent")
    memory = metrics.get("memory_usage_percent")
    disk = metrics.get("disk_usage_percent")
    service_status = metrics.get("service_status")
    latency_ms = metrics.get("latency_ms")

    if cpu is None or not (0 <= cpu <= 85):
        errors.append(f"CPU usage out of range: {cpu}")

    if memory is None or not (0 <= memory <= 90):
        errors.append(f"Memory usage out of range: {memory}")

    if disk is None or not (0 <= disk <= 90):
        errors.append(f"Disk usage out of range: {disk}")

    if service_status != "healthy":
        errors.append(f"Service status invalid: {service_status}")

    if latency_ms is None or latency_ms > 200:
        errors.append(f"Latency too high: {latency_ms} ms")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        logger.error("Usage: python validator.py <metrics_file.json>")
        return 1

    metrics_file = sys.argv[1]

    try:
        logger.info("Loading metrics from %s", metrics_file)
        metrics = load_metrics(metrics_file)

        logger.info("Running validation checks")
        errors = validate_metrics(metrics)

        if errors:
            logger.error("Validation failed")
            for err in errors:
                logger.error(" - %s", err)
            return 2

        logger.info("All validation checks passed")
        return 0

    except Exception as exc:
        logger.exception("Execution failed: %s", exc)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())