import pytest

from aoc.day3 import ex1, ex2

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"


def test_ex1():
    assert ex1(["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]) == 198

    with open('./tests/inputs/day3.txt') as f:
        lines = f.read().splitlines()
        print(f"Solution of day 3, exercise 1 is {ex1(lines)}")
        assert(ex1(lines) == 841526)


def test_ex2():
    assert ex2(["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]) == 230

    with open('./tests/inputs/day3.txt') as f:
        lines = f.read().splitlines()
        print(f"Solution of day 3, exercise 2 is {ex2(lines)}")
        assert(ex2(lines) == 4790390)
