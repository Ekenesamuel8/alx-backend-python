#!/usr/bin/env python3
"""type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list:takes a list input_list of floats as argument
    returns: their sum as a float.
    """
    return float(sum(input_list))
