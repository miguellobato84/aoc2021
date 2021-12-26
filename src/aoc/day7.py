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

def sum_until(n):
    return int(n * (n + 1) / 2)

def ex1(numbers):
    distances = {}
    for x0 in range(min(numbers), max(numbers)+1):
        distances[x0] = sum([abs(x-x0) for x in numbers])

    distances = [(x,y) for (x,y) in sorted(distances.items(), key=lambda x:x[1])]
    return distances[0][1]


def ex2(numbers):
    distances = {}
    for x0 in range(min(numbers), max(numbers)+1):
        distances[x0] = sum([sum_until(abs(x-x0)) for x in numbers])

    distances = [(x,y) for (x,y) in sorted(distances.items(), key=lambda x:x[1])]
    return distances[0][1]