#!/usr/bin/env python3


import argparse
import os
import sys

ZERO = [
    ' __',
    '| |',
    '|_|'
]
ONE = [
    '   ',
    '  |',
    '  |'
]
TWO = [
    '__ ',
    '__|',
    '|__'
]
THREE = [
    '__ ',
    '__|',
    '__|'
]
FOUR = [
    '   ',
    '|_|',
    '  |'
]
FIVE = [
    ' __',
    '|__',
    '__|'
]
SIX = [
    ' __',
    '|__',
    '|_|'
]
SEVEN = [
    ' __',
    '  |',
    '  |'
]
EIGHT = [
    ' __',
    '|_|',
    '|_|'
]
NINE = [
    ' __',
    '|_|',
    '__|'
]

NUMBERS = [
    ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE
]


TEST_NUMBERS = '1234567890'


def _build_array():
    return [
        NUMBERS[num] for num in [
            int(num) for num in TEST_NUMBERS
        ]
    ]


def _to_lcd_lines():
    numbers = _build_array()
    lines = []
    # each number is three lines tall
    # we need to create three lines with num[0] for each number
    for i in range(3):
        lines.append(' '.join([num[i] for num in numbers]))
    return lines


def to_lcd_screen():
    for line in _to_lcd_lines():
        print(line)


def main(arguments):
    print(TEST_NUMBERS)
    print()
    to_lcd_screen()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
