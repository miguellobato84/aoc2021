import decimal
import pytest

from aoc.day8 import ex1, ex2
import numpy as np

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

def parse_input(lines):
    for a,b in [x.split("|") for x in lines]:
        yield [a.strip().split(" "), b.strip().split(" ")]


def test_ex1():
    with open('./tests/inputs/day8a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(numbers)
        assert(result == 26)

    with open('./tests/inputs/day8b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex1(numbers)
        print(f"Solution of day 8, exercise 1 is {result}")
        assert(result == 539)


def test_ex2():
    with open('./tests/inputs/day8a.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex2(numbers)
        assert(result == 61229)

    with open('./tests/inputs/day8b.txt') as f:
        numbers = parse_input(f.read().splitlines())
        result = ex2(numbers)
        print(f"Solution of day 8, exercise 2 is {result}")
        assert(result == 1084606)
