#!/usr/bin/python3
"""
This script reads stdin line by line, processes HTTP request logs, and computes metrics such as
total file size and the number of occurrences of HTTP status codes.
"""

import sys

def print_stats(total_size, status_codes):
    """
    Prints the computed metrics: total file size and the count of each status code
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def process_log():
    """
    Processes log lines from stdin, computes total file size and counts status codes
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()

            # Check if the line has the correct format
            if len(parts) < 7:
                continue

            try:
                # Extract the status code and file size
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update total size
                total_size += file_size

                # Update status code count if it's a valid status code
                if status_code in status_codes:
                    status_codes[status_code] += 1

            except (ValueError, IndexError):
                # Skip the line if parsing fails
                continue

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Print final stats on keyboard interruption (CTRL + C)
        print_stats(total_size, status_codes)
        raise

    # Print final stats after processing all input
    print_stats(total_size, status_codes)

if __name__ == "__main__":
    process_log()
