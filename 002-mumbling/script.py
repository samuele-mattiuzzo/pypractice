#!/usr/bin/env python3


import argparse
import os
import sys

TEST_INPUTS = [
    'QWERTY',
    'abc',
    'a',
    'hello moto',
    '',
    None
]


def mumble_letters(letters):
    if letters in ['', None]:
        return 'Please provide some input'

    return '-'.join([
        (letter * (idx + 1)).title()
        for idx, letter in enumerate(letters)
    ])


def main(arguments):
    for ipt in TEST_INPUTS:
        print('[{}]: {}'.format(
            ipt, mumble_letters(ipt)
        ))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
