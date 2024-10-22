#!/usr/bin/env python3
"""type-anotation"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier: that takes a float multiplier as argument
    args:
        multiplier (float)
    returns:
        a function that multiplies a float by multiplier.
    """
    def funct(value: float) -> float:
        return (value * multiplier)
    return funct
