#!/usr/bin/env python3
"""type-annotated function"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of strings and returns a list of tuples.
    Each tuple contains a string from the input list and its length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains a string and its length.
    """
    return [(i, len(i)) for i in lst]