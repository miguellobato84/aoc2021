import pytest

from aoc.day4 import ex1, ex2
import numpy as np

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

def parse_input(lines):
    numbers = np.array(lines[0].split(",")).astype(int).tolist()
    cards = list(map(lambda x:np.array(list(filter(lambda y: y != "", x.split(" ")))).astype(int).tolist(), filter(lambda x:x != '', lines[1:])))
    cards = np.array_split(cards, len(cards)/5)
    return numbers, cards


def test_ex1():
    with open('./tests/inputs/day4a.txt') as f:
        numbers, cards = parse_input(f.read().splitlines())
        result = ex1(numbers, cards)
        assert(result == 4512)

    with open('./tests/inputs/day4b.txt') as f:
        numbers, cards = parse_input(f.read().splitlines())
        result = ex1(numbers, cards)
        print(f"Solution of day 4, exercise 1 is {result}")
        assert(result == 4662)


def test_ex2():
    with open('./tests/inputs/day4a.txt') as f:
        numbers, cards = parse_input(f.read().splitlines())
        result = ex2(numbers, cards)
        assert(result == 1924)

    with open('./tests/inputs/day4b.txt') as f:
        numbers, cards = parse_input(f.read().splitlines())
        result = ex2(numbers, cards)
        print(f"Solution of day 4, exercise 2 is {result}")
        assert(result == 12080)
