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


def ex1(days, numbers):
    state = {x:sum([1 if y==x else 0 for y in numbers]) for x in range(9)}
    for day in range(days):
        state = {x:(state[7] + state[0] if x==6 else state[0] if x == 8 else state[x+1]) for x in range(9)}
    return sum(state.values())

def ex2(days, numbers):
    return ex1(days, numbers)