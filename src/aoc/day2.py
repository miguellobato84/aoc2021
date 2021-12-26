import argparse
import logging
import sys

from aoc import __version__
from numpy.lib.stride_tricks import sliding_window_view

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


def ex1(inputs):
    horizontal = sum(map(lambda x: x[1], filter(lambda x: x[0] == "forward", inputs)))
    depth = sum(map(lambda x: x[1] if x[0] == "down" else -1 * x[1], filter(lambda x: x[0] != "forward", inputs)))
    return horizontal * depth



def ex2(inputs):
    horizontal = sum(map(lambda x: x[1], filter(lambda x: x[0] == "forward", inputs)))
    aim = 0
    depth = 0

    for t in inputs:
        if t[0] == "down":
            aim += t[1]
        elif t[0] == "up":
            aim -= t[1]
        else:
            depth += t[1] * aim

    return horizontal * depth

