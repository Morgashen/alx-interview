#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else
return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you
only need to handle the 8 least significant bits of each
integer
"""


def validUTF8(data):
    """_summary_

    Args:
            data (list[int]): a list of integers
    """
    expected_continuation_bytes = 0

    UTF8_BIT_1 = 1 << 7
    UTF8_BIT_2 = 1 << 6

    for byte in data:

        leading_one_mask = 1 << 7

        if expected_continuation_bytes == 0:

            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask = leading_one_mask >> 1



            if expected_continuation_bytes == 0:
                continue
    
            if expected_continuation_bytes == 1 or\
                    expected_continuation_bytes > 4:
                return False


        else:
    
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        expected_continuation_bytes -= 1

    if expected_continuation_bytes == 0:
        return True
    else:
        return False
