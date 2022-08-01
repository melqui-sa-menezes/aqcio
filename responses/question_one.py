def _hex_conversion(
        digit: str,
        index: int,
        base: int = 16,
) -> int:
    conversion_table = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    return conversion_table[digit] * base ** index


def parse_hex_int(value: str) -> int:
    hexadecimal = value.strip().upper()
    index = len(hexadecimal) - 1
    decimal = 0
    for digit in hexadecimal:
        decimal += _hex_conversion(digit, index)
        index -= 1

    return decimal


assert parse_hex_int("A") == 10
assert parse_hex_int("1F") == 31
assert parse_hex_int("0") == 0
assert parse_hex_int("3D") == 61
assert parse_hex_int("BB26") == 47910
