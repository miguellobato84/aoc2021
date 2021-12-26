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
    prev = inputs[0]
    result = 0
    for t in inputs[1:]:
        if t > prev:
            result += 1
        prev = t
    return result



def ex2(inputs):
    inputs = sliding_window_view(inputs, 3)
    inputs = list(map(lambda x: sum(x), inputs))
    return ex1(inputs)
