"""This file contains my representation of a suffix tree."""
__author__ = "Jørgen Aleksander Fagervik"

"""
T = abaaba$
m = len(T) 

How many leaves? : m
How many non-leaf nodes? : m-1 <= 2m -1 nodes total, or O(m) nodes

Total length of edge labels is quadratic in m
"""


class Node:
    def __init__(self, label: str = "") -> None:
        self.label = label


class Edge:
    def __init__(
        self, parent: Node, children: list[Node] = None, label: tuple = None
    ) -> None:
        self.parent = parent
        self.children = children if children is not None else []
        self.label = label


class SuffixTree:
    """
    We will be using lcp and suffix arrays to construct the SuffixTree here, not ukkonen

    Suffix Array: 1. sort array of suffixes. 2. replace each letter by its rank in Sigma (The alphabet)
    3.
    O(m) space
    O(m^2) time
    """

    def __init__(self, t: str) -> None:
        t.__add__("$")
        self.suffixes = [t[i:] for i in range(len(t))]

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
