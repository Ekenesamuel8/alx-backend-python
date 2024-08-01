#!/usr/bin/env python3
"""type-anntonation"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv: takes a string
    k: a string
    v: an int or float
    returns: a tuple.
    (The second element is the square of the int/float v
    and should be annotated as a float.)
    """
    return (k, float(v ** 2))
