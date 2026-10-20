"""CLI entry point."""

import click
from .recon import enumerate_subdomains, resolve_host
from .scanner import scan_host
from .vuln import run_checks


@click.group()
def cli():
    """Security Automation Toolkit CLI."""


@cli.command()
@click.option("--target", required=True)
@click.option("--output", default=None)
def recon(target, output):
    subs = enumerate_subdomains(target)
    click.echo(f"Found {len(subs)} subdomains for {target}")
    for s in subs:
        click.echo(s)


@cli.command()
@click.option("--host", required=True)
@click.option("--ports", default="1-1000")
def scan(host, ports):
    start, end = (int(x) for x in ports.split("-"))
    open_ports = scan_host(host, range(start, end + 1))
    click.echo(f"Open ports on {host}: {open_ports}")


@cli.command()
@click.option("--host", required=True)
@click.option("--ports", default="80,443,22")
def vuln(host, ports):
    open_ports = [int(p) for p in ports.split(",")]
    results = run_checks(host, open_ports)
    for r in results:
        click.echo(r)


if __name__ == "__main__":
    cli()
