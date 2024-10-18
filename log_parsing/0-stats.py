#!/usr/bin/python3

"""Log parsing"""

import sys

i = 0  
FileSize = 0 
STATUS = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}

def print_stats(FileSize, STATUS):
    """Prints the accumulated file size and status codes"""
    print("File size: {}".format(FileSize))
    for key in sorted(STATUS.keys()):
        if STATUS[key] > 0:
            print("{}: {}".format(key, STATUS[key]))

try:
    for line in sys.stdin:
        i += 1
        sp = line.split()

        if len(sp) > 2:
            try:
                FileSize += int(sp[-1])
            except (ValueError, IndexError):
                pass

            if sp[-2] in STATUS:
                STATUS[sp[-2]] += 1

        if i % 10 == 0:
            print_stats(FileSize, STATUS)

except KeyboardInterrupt:
    print_stats(FileSize, STATUS)
    raise

finally:
    print_stats(FileSize, STATUS)
