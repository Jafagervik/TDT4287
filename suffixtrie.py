"""Represents the suffix trie data structure for strings"""


from typing import Any, Optional


class SuffixTrie:
    def __init__(self, t: str) -> Any:
        """Make suffix trie from s."""
        t.__add__("$")
        self.root = {}
        for i in range(len(t)):
            cur = self.root
            for c in t[i:]:
                if c not in cur:
                    cur[c] = {}  # add outgoing edge
                cur = cur[c]

    def follow_path(self, s: str) -> Any:
        """
        Follow path given by characters of s.
        Returns -> Node | None
        """
        cur = self.root
        for c in s:
            if c not in cur:
                return None
            cur = cur[c]
        return cur

    def has_substring(self, s: str) -> bool:
        """Returns true iff s appears as a substring of trie."""
        return self.follow_path(s) is not None

    def has_suffix(self, s: str) -> bool:
        """Returns true iff s is a suffix of t."""
        node = self.follow_path(s)
        return node is not None and "$" in node

    def __len__(self):
        """Returns the amount of node in the suffix trie."""
