import decimal
import pytest

from aoc.day9 import ex1, ex2
import numpy as np

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

def parse_input(lines):
    lines = [[int(item) for item in line] for line in lines]
    return np.array(lines)


def test_ex1():
    with open('./tests/inputs/day9a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(numbers)
        assert(result == 15)

    with open('./tests/inputs/day9b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(numbers)
        print(f"Solution of day 9, exercise 1 is {result}")
        assert(result == 575)


def test_ex2():
    with open('./tests/inputs/day9a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex2(numbers)
        assert(result == 1134)

    with open('./tests/inputs/day9b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex2(numbers)
        print(f"Solution of day 9, exercise 2 is {result}")
        assert(result == 1019700)
