"""Reconnaissance helpers: subdomain enumeration and DNS resolution."""

import socket
import concurrent.futures


def resolve_host(host: str) -> str | None:
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None


def enumerate_subdomains(domain: str, wordlist: list[str] | None = None) -> list[str]:
    wordlist = wordlist or ["www", "mail", "api", "dev", "staging", "vpn", "admin"]
    found = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
        futures = {ex.submit(resolve_host, f"{w}.{domain}"): w for w in wordlist}
        for fut, w in futures.items():
            if fut.result():
                found.append(f"{w}.{domain}")
    return found
