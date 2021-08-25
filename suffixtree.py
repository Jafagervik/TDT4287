"""This file contains my representation of a suffix tree."""
__author__ = "Jørgen Aleksander Fagervik"

"""
T = abaaba$
m = len(T) 

How many leaves? : m
How many non-leaf nodes? : m-1 <= 2m -1 nodes total, or O(m) nodes

Total length of edge labels is quadratic in m
"""


class SuffixTree:
    """

    O(m) space
    O(m^2) time
    """

    def __init__(self) -> None:
        pass

    def follow(self, s):
        pass

    def is_suffix(self) -> bool:
        pass

    def is_substring(self, s) -> bool:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    def __len__(self) -> int:
        pass
