# Log Parsing

## Description

This project involves writing a Python script that reads logs from standard input (`stdin`) line by line and computes various metrics, including total file size and counts of HTTP status codes.

## Requirements

- Python 3.4.3
- PEP 8 code style
- Executable scripts
- Running on Ubuntu 14.04 LTS

## Files

- **`0-stats.py`**: Reads and processes log input to compute metrics.
- **`0-generator.py`**: Generates sample log data for testing.

## Usage

```bash
./0-generator.py | ./0-stats.py
