import argparse
import logging
import sys

from aoc import __version__
import numpy as np
import collections

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def _get_points(x1, y1, x2, y2):
    def slope(a, b):
        return -1 if a < b else 0 if a == b else 1

    for i in range(max(abs(x2 - x1), abs(y2 - y1)) + 1):
        yield x1 + i * slope(x2, x1), y1 + i * slope(y2, y1)


def ex1(lines):
    matrix = collections.defaultdict(int)
    for x1, y1, x2, y2 in [(x1, y1, x2, y2) for (x1, y1, x2, y2) in lines if x1 == x2 or y1 == y2]:
        for x, y in _get_points(x1, y1, x2, y2):
            matrix[x, y] += 1

    return sum(x > 1 for x in matrix.values())


def ex2(lines):
    matrix = collections.defaultdict(int)
    for x1, y1, x2, y2 in lines:
        for x, y in _get_points(x1, y1, x2, y2):
            matrix[x, y] += 1

    return sum(x > 1 for x in matrix.values())
