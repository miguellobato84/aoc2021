import pytest

from aoc.day5 import ex1, ex2
import numpy as np

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

def parse_input(lines):
    import re
    pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')  
    return [[int(n) for n in m.groups()] for m in map(pattern.match, lines)]


def test_ex1():
    with open('./tests/inputs/day5a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(numbers)
        assert(result == 5)

    with open('./tests/inputs/day5b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(numbers)
        print(f"Solution of day 5, exercise 1 is {result}")
        assert(result == 6113)


def test_ex2():
    with open('./tests/inputs/day5a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex2(numbers)
        assert(result == 12)

    with open('./tests/inputs/day5b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex2(numbers)
        print(f"Solution of day 5, exercise 2 is {result}")
        assert(result == 20373)
