import pytest

from aoc.day6 import ex1, ex2
import numpy as np

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

def parse_input(lines):
    return list(map(lambda x:int(x), lines[0].split(",")))


def test_ex1():
    with open('./tests/inputs/day6a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(80, numbers)
        assert(result == 5934)

    with open('./tests/inputs/day6b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(80, numbers)
        print(f"Solution of day 6, exercise 1 is {result}")
        assert(result == 360610)


def test_ex2():
    with open('./tests/inputs/day6a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(256, numbers)
        assert(result == 26984457539)

    with open('./tests/inputs/day6b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(256, numbers)
        print(f"Solution of day 6, exercise 2 is {result}")
        assert(result == 1631629590423)
