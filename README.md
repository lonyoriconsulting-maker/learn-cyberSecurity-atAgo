# SecuScan

A lightweight CLI tool to scan directories for sensitive data patterns (passwords, emails, API-key-like strings) that shouldn't be committed to source control.

## Usage
```bash
python3 secuscan.py --path ./your_folder --output report.txt
```

## Why
Hardcoded secrets in source code are a common real-world breach vector. This tool is a simplified version of tools like gitleaks/truffleHog, built to understand the detection logic behind them.