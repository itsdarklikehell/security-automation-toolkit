"""Vulnerability check helpers (lightweight, non-intrusive)."""

COMMON_CHECKS = [
    {"name": "open-http", "port": 80, "banner": "HTTP"},
    {"name": "open-https", "port": 443, "banner": "HTTPS"},
    {"name": "open-ssh", "port": 22, "banner": "SSH"},
]


def run_checks(host: str, open_ports: list[int]) -> list[dict]:
    results = []
    for c in COMMON_CHECKS:
        if c["port"] in open_ports:
            results.append({"host": host, "check": c["name"], "status": "open"})
    return results
