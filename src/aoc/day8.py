import argparse
import logging
import sys

from numpy.lib.arraysetops import union1d, unique
from numpy.lib.index_tricks import c_

from aoc import __version__
import numpy as np
import collections

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

from collections import defaultdict

def state_to_code(state, word):
    return "".join([str(state[letter]) for letter in word])

def code_to_number(code):
    code = list(map(lambda x:int(x), list(code)))
    valid_values = {
        1:[3,6],
        2:[1,3,4,5,7],
        3:[1,3,4,6,7],
        4:[2,3,4,6],
        5:[1,2,4,6,7],
        6:[1,2,4,5,6,7],
        7:[1,3,6],
        8:[1,2,3,4,5,6,7],
        9:[1,2,3,4,6,7],
        0:[1,2,3,5,6,7],
    }
    for n in valid_values:
        valid_value = len(code) == len(valid_values[n]) and len(code) == len(np.intersect1d(code, valid_values[n]))
        if valid_value: return n
    return -1

def is_valid_state(numbers, state):
    codes = [state_to_code(state, word) for word in numbers]
    decoded = [code_to_number(code) for code in codes]
    #logging.debug(f"Codes: {codes}, numbers: {numbers}, decoded: {decoded}, state: {state}")
    return all([x >= 0 for x in decoded])

def _brute_force(numbers, state, pending_steps = "abcdefg"):
    result = []
    if pending_steps[0] == "g":
        for combi in state["g"]:
            c_state = {**state, **{"g":combi}}
            result.append(c_state)
    else:
        for combi in state[pending_steps[0]]:
            c_state = {**state, **{pending_steps[0]:combi}}
            result = result + _brute_force(numbers, c_state, pending_steps[1:])
    
    return result

def brute_force(numbers, state):
    combis = _brute_force(numbers, state)
    combis = [x for x in combis if len(np.unique(list(x.values()))) == 7 and is_valid_state(numbers, x)]
    logging.debug(f"Found {len(combis)} combination")
    assert len(combis) == 1
    return combis[0]


def ex1(lines):
    lines = [line[1] for line in lines]
    lengths = [len(item) for sublist in lines for item in sublist]
    numbers = [1 if x in (2,4,3,7) else 0 for x in lengths]
    return sum(numbers)

def ex2(lines):
    n = []
    for a,b in lines:
        n.append(_ex2(a,b))
    return sum(n)

def _ex2(numbers, output):
    logging.debug(numbers)
    all = list(range(1,8))
    state = {}

    #step 1: only valid values
    for n in [x for x in numbers if len(x) in [2,3,4]]:
        if len(n) == 4:
            possibilities = {x:[2,4,3,6] for x in n}
        elif len(n) == 3:
            possibilities = {x:[1,3,6] for x in n}
        elif len(n) == 2:
            possibilities = {x:[3,6] for x in n}
        state = {**state, **{x:np.intersect1d(state[x] if x in state else all, possibilities[x]) for x in n}}
    logging.debug(f"Step 1: {state}")

    #step 2: isolate unique
    unique = np.bincount([x for sublist in state.values() for x in sublist])
    unique = [i for x,i in enumerate(unique) if x == 1]
    state = {**state, **{x:unique for x in state if len(np.intersect1d(unique, state[x])) == 1}}
    logging.debug(f"Step 2: {state}")

    #step 3: isolate pairs
    #TODO

    #step 4: generate others combinations
    used_values = [x for sublist in state.values() for x in sublist]
    not_used_values = [i for i in all if i not in used_values]
    state = {**{x:not_used_values for x in "abcdefg"}, **state}
    logging.debug(f"Step 4: {state}")
    
    #step 5: brute force
    state = brute_force(numbers, state)
    logging.debug(f"Step 5: {state}")
    
    #step 6: translate output
    logging.debug(output)
    codes = [state_to_code(state, word) for word in output]
    n = int("".join([str(code_to_number(code)) for code in codes]))
    logging.debug(n)


    return n