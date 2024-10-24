#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn't appear or is not an integer,
don't print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""
import sys


def print_stats(total_size, status_codes_dict):
    """Print the computed statistics"""
    print('File size: {}'.format(total_size))
    for key in sorted(status_codes_dict.keys()):
        if status_codes_dict[key] > 0:
            print('{}: {}'.format(key, status_codes_dict[key]))


def main():
    """Main function to process input and compute metrics"""
    status_codes_dict = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    total_size = 0
    count = 0

    try:
        for line in sys.stdin:
            try:
                # Split line and validate format
                line_list = line.split()
                if len(line_list) >= 7:
                    # Extract and validate status code and file size
                    status_code = line_list[-2]
                    file_size = line_list[-1]

                    # Update metrics if status code is valid
                    if status_code in status_codes_dict:
                        status_codes_dict[status_code] += 1
                    
                    # Update total size if file size is valid
                    try:
                        total_size += int(file_size)
                    except ValueError:
                        continue

                    # Update count and print stats every 10 lines
                    count += 1
                    if count == 10:
                        print_stats(total_size, status_codes_dict)
                        count = 0

            except (IndexError, ValueError):
                continue

    except KeyboardInterrupt:
        print_stats(total_size, status_codes_dict)
        raise
    
    print_stats(total_size, status_codes_dict)


if __name__ == "__main__":
    main()
