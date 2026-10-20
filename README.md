# Security Automation Toolkit

A Python toolkit for automating reconnaissance and vulnerability-scanning workflows. Built for security researchers and red-teamers who want repeatable, scriptable pipelines for subdomain enumeration, port scanning, service fingerprinting, and vulnerability checks.

## Features

- Modular recon pipeline (subdomain enumeration, DNS resolution, port scanning)
- Service fingerprinting and banner grabbing
- Pluggable vulnerability checks
- Concurrent execution with configurable rate limiting
- JSON/CSV report output
- CLI interface for ad-hoc and scripted runs

## Installation

```bash
git clone https://github.com/itsdarklikehell/security-automation-toolkit.git
cd security-automation-toolkit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Full recon pipeline against a target
python -m security_automation_toolkit recon --target example.com --output results.json

# Port scan only
python -m security_automation_toolkit scan --host 192.168.1.1 --ports 1-1000

# Run vulnerability checks against discovered services
python -m security_automation_toolkit vuln --input results.json
```

See `--help` on each subcommand for full options.

## Project Structure

```
security-automation-toolkit/
├── security_automation_toolkit/
│   ├── __init__.py
│   ├── cli.py
│   ├── recon.py
│   ├── scanner.py
│   └── vuln.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Disclaimer

This toolkit is intended for authorized security testing and research only. Always obtain written permission before scanning systems you do not own. The author is not responsible for misuse.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
