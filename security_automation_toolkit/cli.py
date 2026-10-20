"""CLI entry point (argparse, stdlib only)."""

import argparse
from .recon import enumerate_subdomains
from .scanner import scan_host
from .vuln import run_checks


def cmd_recon(args):
    subs = enumerate_subdomains(args.target)
    print(f"Found {len(subs)} subdomains for {args.target}")
    for s in subs:
        print(s)


def cmd_scan(args):
    start, end = (int(x) for x in args.ports.split("-"))
    open_ports = scan_host(args.host, range(start, end + 1))
    print(f"Open ports on {args.host}: {open_ports}")


def cmd_vuln(args):
    open_ports = [int(p) for p in args.ports.split(",")]
    for r in run_checks(args.host, open_ports):
        print(r)


def main():
    parser = argparse.ArgumentParser(prog="security-automation-toolkit")
    sub = parser.add_subparsers(dest="command", required=True)

    p_recon = sub.add_parser("recon")
    p_recon.add_argument("--target", required=True)
    p_recon.set_defaults(func=cmd_recon)

    p_scan = sub.add_parser("scan")
    p_scan.add_argument("--host", required=True)
    p_scan.add_argument("--ports", default="1-1000")
    p_scan.set_defaults(func=cmd_scan)

    p_vuln = sub.add_parser("vuln")
    p_vuln.add_argument("--host", required=True)
    p_vuln.add_argument("--ports", default="80,443,22")
    p_vuln.set_defaults(func=cmd_vuln)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
