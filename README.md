# SecuScan

A command-line tool that recursively scans a directory for accidentally committed secrets — hardcoded passwords, email addresses, and API-key-like strings — and writes a findings report.

> **Year 1 · Module 1: Programming & Scripting Basics**
> First stop on a 4-year, project-based Cyber Security roadmap.See [the 4-year roadmap](https://github.com/lonyoriconsulting-maker/btech-cybersec-roadmap) for where this project goes next.

## Why this exists

Secrets leaking into source code or config files is one of the most common, most preventable breach vectors — a `.env` committed by accident, a password left in a comment, a stray API key in a config. Professional tools like `gitleaks` and `truffleHog` exist entirely to catch this before it ships. SecuScan is a small, from-scratch version of the same idea: walk a directory tree, read every file safely, and flag lines that match risky patterns.

## What it detects

| Category | Pattern logic |
|---|---|
| Hardcoded passwords | `password = ...` (case-insensitive) |
| Email addresses | standard email regex |
| Possible API keys | long unbroken alphanumeric strings (32+ chars) |

## How it works

1. **Walk** — `os.walk` recurses through every subfolder from the target path.
2. **Read safely** — each file is opened defensively; unreadable, binary, or permission-denied files are skipped instead of crashing the scan.
3. **Match** — every line is checked against the pattern set above.
4. **Report** — all findings are written to a plain-text report with file path, line number, and matched category.

## Usage

```bash
git clone <your-repo-url>
cd secuscan
python3 -m venv venv
source venv/bin/activate
python3 secuscan.py --path /path/to/scan --output findings.txt
```

**Arguments**

- `--path` (required) — directory to scan
- `--output` (default: `report.txt`) — where to write the findings report

## Project status

Built and working: directory walk, safe file reading, multi-pattern regex matching, CLI args, report output. This is a completed Year 1 milestone, not a finished security product — see [Limitations](#limitations) and the [4-year roadmap](https://github.com/lonyoriconsulting-maker/btech-cybersec-roadmap) for where the rough edges get sanded off in later years.

## Limitations

- Regex-only matching → false positives on things like base64 image data or long hashes, and false negatives on obfuscated secrets
- No entropy scoring (a real key vs. a random-looking string look identical to a fixed regex)
- No `.gitignore`-aware skipping — currently scans `venv/`, `.git/`, etc. too
- No config file for adding/removing patterns without editing source

These aren't bugs so much as the honest boundary of what a Module 1 tool should do. Each one maps to a specific upgrade later in the curriculum.

## Stack

Python 3, `os`, `re`, `argparse` — no external dependencies. Built in WSL (Ubuntu) with VS Code, versioned with Git/GitHub.
