#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes_count = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
line_count = 0

# Function to print statistics
def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

# Signal handler for keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Main loop to read from stdin line by line
try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        # Check if the line matches the expected format
        if len(parts) < 9 or parts[5] != '"GET' or parts[7] != 'HTTP/1.1"':
            continue
        
        # Extract file size and status code
        try:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size

            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        except (ValueError, IndexError):
            continue

        # After every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
