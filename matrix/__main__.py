import argparse
import sys
from time import sleep
from random import choice, randint
from typing import Optional

import codes

DRAW_INTERVAL = 0.05

COLUMN_MIN_HEIGHT = 20

ASCII = [
    c for c
    in map(chr, range(33, 127))
    if c.isprintable()
]

LATIN = [
    c for c
    in map(chr, range(0x00C0, 0x00FF + 1))
    if c.isalpha()
]

GREEK = [
    c for c
    in map(chr, range(0x0370, 0x03FF + 1))
    if c.isalpha()
]

CYRILLIC = [
    c for c
    in map(chr, range(0x0400, 0x04FF + 1))
    if c.isalpha()
]


class Column:
    window_height: int  # Sliding window height
    offset: int
    chars: list
    height: int
    finished: bool

    def __init__(self, height):
        self.height = height
        self.finished = False
        self.window_height = randint(COLUMN_MIN_HEIGHT, self.height)
        self.offset = -self.window_height
        self.chars = [' ' for _ in range(self.height)]

    @property
    def end_offset(self):
        return self.offset + self.window_height

    def __getitem__(self, index):
        """Get the character at the given index.

        Also applies formatting to the character.
        """
        c = self.chars[index]
        if index == self.end_offset:
            return f'{codes.FG_WHITE}{codes.BOLD}{c}{codes.RESET}{codes.FG_DEFAULT}'
        if self.end_offset <= index <= self.end_offset - 2:
            return f'{codes.FG_WHITE}{c}{codes.FG_DEFAULT}'
        if self.offset <= index <= self.offset + 2:
            return f'{codes.FG_GREEN}{codes.DIM}{c}{codes.RESET}{codes.FG_DEFAULT}'
        return f'{codes.FG_GREEN}{c}{codes.FG_DEFAULT}'

    def update(self):
        if self.finished:
            return

        # Remove old top character
        if self.offset >= 0:
            self.chars[self.offset] = ' '

        # Update offset
        self.offset += 1
        if self.offset >= self.height:
            self.finished = True
            return

        # Add new bottom character
        if self.end_offset < self.height:
            self.chars[self.end_offset] = choice(ALPHABET)

        # Update a single random character in the window
        idx = self.offset + randint(0, self.window_height - 1)
        if 0 <= idx < self.height:
            self.chars[idx] = choice(ALPHABET)


def update_columns(columns: list[Optional[Column]]):
    idx = randint(0, len(columns) - 1)
    if columns[idx] is None:
        columns[idx] = Column(HEIGHT)

    for i, column in enumerate(columns):
        if column is None:
            continue
        column.update()
        if column.finished:
            columns[i] = None


def print_columns(columns: list[Optional[Column]]):
    lines = ['' for _ in range(HEIGHT)]
    for column in columns:
        for i in range(HEIGHT):
            lines[i] += ' ' if column is None else column[i]
    print(codes.MOVE(1, 1), end='')
    print('\n'.join(lines), end='', flush=True)


try:
    parser = argparse.ArgumentParser()
    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    parser.add_argument('--no-latin', action='store_true', help='Disable Latin extended characters')
    parser.add_argument('--no-greek', action='store_true', help='Disable Greek characters')
    parser.add_argument('--no-cyrillic', action='store_true', help='Disable Cyrillic characters')
    args = parser.parse_args()

    WIDTH = args.width
    HEIGHT = args.height - 1

    ALPHABET = ASCII
    if not args.no_latin:
        ALPHABET += LATIN
    if not args.no_greek:
        ALPHABET += GREEK
    if not args.no_cyrillic:
        ALPHABET += CYRILLIC

    print(codes.EN_ALT_SCREEN_BUF, end='')
    print(codes.HIDE, end='')

    columns = [None for _ in range(WIDTH)]
    while True:
        update_columns(columns)
        print_columns(columns)
        sleep(DRAW_INTERVAL)
except KeyboardInterrupt:
    pass
finally:
    print(codes.DIS_ALT_SCREEN_BUF, end='')
    print(codes.SHOW, end='')
