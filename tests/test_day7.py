import decimal
import pytest

from aoc.day7 import ex1, ex2
import numpy as np

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

def parse_input(lines):
    return list(map(lambda x:int(x), lines[0].split(",")))


def test_ex1():
    with open('./tests/inputs/day7a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(numbers)
        assert(result == 37)

    with open('./tests/inputs/day7b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(numbers)
        print(f"Solution of day 7, exercise 1 is {result}")
        assert(result == 328262)


def test_ex2():
    with open('./tests/inputs/day7a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex2(numbers)
        assert(result == 168)

    with open('./tests/inputs/day7b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex2(numbers)
        print(f"Solution of day 7, exercise 2 is {result}")
        assert(result == 90040997.0)

