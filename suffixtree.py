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
    def __init__(self, label: int, parent=None, children=None) -> None:
        self.label = label
        self.parent = parent
        # Children in this case actually become the edges
        self.children = [] if not children else children


class Edge:
    def __init__(self, f: Node, t: Node, label: str = "", substr: tuple = (0, 0)):
        self.f = f
        self.t = t
        self.label = label
        self.substr = substr

    def __repr__(self):
        pass


class SuffixTree:
    """
    Using good ol Ukkonens algorithm

    """

    def __init__(self, t: str) -> None:
        t.__add__("$")
        self.t = t
        self.n = len(self.t)
        self.root = None
        self.remainder = 0
        self.active_node = None
        self.active_edge = None
        self.active_length = 0
        self.end = 0

    def get_child(self, node, i):
        # The way to access a child self.root.children[0].t
        return node.children[i].t

    def get_first_child(self, node):
        return node.children[0].t

    def get_all_children(self, node):
        return [edge.t for edge in node.children]

    def build_suffix_tree(self):
        """
        Making tree in O(n) time by making use of suffix links
        """
        prev_node = None

        for i in range(self.n):
            new_node = Node(i)
            # Root
            if i == 0:
                self.root = new_node
                prev_node = new_node
            self.active_node = new_node

            new_edge = Edge(prev_node, new_node, self.t[:i], (i, len(self.t)))
            prev_node.children.append(new_edge)
            new_node.parent = prev_node
            # Case 1: No outgoing edge, check first character in all children edges
            if self.t[i] not in [c.label[0] for c in self.active_node.children]:
                # time 8:12 in https://www.youtube.com/watch?v=ByuMPBfyR5g

                continue

    def print_edges(self):
        raise NotImplementedError()