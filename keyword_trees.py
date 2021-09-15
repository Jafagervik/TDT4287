class Tree:
    class Node:
        def __init__(self, edge_label: str, children=None) -> None:
            if children is None:
                self.children = children
            self.children = []
            self.edge_label = edge_label

    def __init__(self, T: str, P: list[str]) -> None:
        self.P = P
        self.T = T
        self.m = len(T)
        self.root, self.tree = self.initialize_tree(P)
        self.n = len(P)

    def initialize_tree(self, P: list[str]):
        self.root = Tree.Node("")
        curr = self.root
        for pattern in P:
            pass

    def initialize_reverse_tree(self):
        curr = self.root
        paths = self.T.split(" ")
        for path in paths:
            children = []
            for i in range(len(path)):
                new = Tree.Node(path[i])
                new.children = children
                new.children.append(path[i + 1])

    def naive_search(self):
        for i in range(self.n):
            pass
