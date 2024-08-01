#!/usr/bin/env python3
"""type-annotated variable"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list: takes a list mxd_lst of integers and floats
    returns: their sum as a float.
    """
    return (sum(mxd_lst))
