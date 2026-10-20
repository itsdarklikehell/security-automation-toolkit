"""Port scanning helpers."""

import socket


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def scan_host(host: str, ports: range | list[int], timeout: float = 1.0) -> list[int]:
    return [p for p in ports if scan_port(host, p, timeout)]
