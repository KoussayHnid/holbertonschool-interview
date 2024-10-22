#!/usr/bin/python3
import sys
import signal

total_file_size = 0
status_codes_count = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

def print_stats():
    """Function to print the statistics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def handle_exit(signal, frame):
    """Handle the CTRL + C (KeyboardInterrupt) to print stats before exiting"""
    print_stats()
    sys.exit(0)
signal.signal(signal.SIGINT, handle_exit)

line_count = 0

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 9:
            continue

        file_size = int(parts[-1])
        status_code = parts[-2]

        total_file_size += file_size

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

    except Exception:
        continue

print_stats()