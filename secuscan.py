import os
import re
import argparse

PATTERNS = {
    "Password": re.compile(r"password\s*=\s*.+", re.IGNORECASE),
    "Email": re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"),
    "Possible API Key": re.compile(r"[A-Za-z0-9_\-]{32,}"),
}

def read_file_lines(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines()
    except (UnicodeDecodeError, PermissionError, IsADirectoryError):
        return []

def scan_line(filepath, line_num, line):
    findings = []
    for label, pattern in PATTERNS.items():
        if pattern.search(line):
            findings.append((filepath, line_num, label, line.strip()))
    return findings

def walk_directory(target_path):
    all_findings = []
    for root, dirs, files in os.walk(target_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            lines = read_file_lines(filepath)
            for line_num, line in enumerate(lines, start=1):
                all_findings.extend(scan_line(filepath, line_num, line))
    return all_findings

def write_report(findings, output_path="report.txt"):
    with open(output_path, "w") as f:
        if not findings:
            f.write("No sensitive data patterns found.\n")
        for filepath, line_num, label, content in findings:
            f.write(f"[{label}] {filepath}:{line_num} -> {content}\n")

def main():
    parser = argparse.ArgumentParser(description="SecuScan: scan a folder for sensitive data patterns.")
    parser.add_argument("--path", required=True, help="Target directory to scan")
    parser.add_argument("--output", default="report.txt", help="Output report file")
    args = parser.parse_args()

    findings = walk_directory(args.path)
    write_report(findings, args.output)

    print(f"Scan complete. {len(findings)} issue(s) found.")
    print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()