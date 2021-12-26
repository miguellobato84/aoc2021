import argparse
import logging
import sys

from aoc import __version__
import numpy as np

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

def ex1(inputs):
    transposed = np.transpose([list(map(lambda x:int(x), n)) for n in inputs])
    argmax = np.array([np.bincount(row).argmax() for row in transposed])
    argmin = np.array([np.bincount(row).argmin() for row in transposed])
    
    gamma = int(''.join(map(lambda x: str(x), argmax)), 2)
    epsilon = int(''.join(map(lambda x: str(x), argmin)), 2)
    
    return gamma*epsilon

def get_mostless_common_value(inputs, position):
    transposed = np.transpose([list(map(lambda x:int(x), n)) for n in inputs])
    bincount = np.bincount(transposed[position])
    most = 1 if bincount[0] == bincount[1] else bincount.argmax()
    less = 0 if bincount[0] == bincount[1] else bincount.argmin()
    return str(most), str(less)

def ex2(inputs):
    oxygen = inputs
    print(f"Input: {inputs}")
    for t in range(len(oxygen[0])):
        most, less = get_mostless_common_value(oxygen, t)
        oxygen = list(filter(lambda x:x[t] == most, oxygen))
        print(f"[Oxygen] Iteration={t}, most={most}, filtering={oxygen}")
        if len(oxygen) == 1:
            break
    
    co2 = inputs
    for t in range(len(co2[0])):
        most, less = get_mostless_common_value(co2, t)
        co2 = list(filter(lambda x:x[t] == less, co2))
        print(f"[CO2] Iteration={t}, less={less}, filtering={co2}")
        if len(co2) == 1:
            break

    oxygen = int(''.join(map(lambda x: str(x), oxygen)), 2)
    co2 = int(''.join(map(lambda x: str(x), co2)), 2)
    
    print(f"oxygen={oxygen}, co2={co2}")
    return oxygen*co2