"""

Homologus Genes
    - Often similar functions 
    - Sequence similarities

Sequence similarity indicates homology
"""


def exact_pattern_match(text: str, pattern: str):
    m = len(text)
    n = len(pattern)
    count = 0

    for i in range(m):
        for j in range(n):
            if text[i] != pattern[j]:
                break
            if count == n:
                print(f"Found pattern that starts at index {i}")
                return i

            count += 1
    return -1


def init_matrix(m: int, n: int):
    return [[False] * (n) for i in range(m)]


def find_diagonals(matrix) -> list:
    pass


def homology_search(S: str, D: str) -> list[str]:
    """
    Dot plot matrix to figure it out
    >> input: Gene sequence S and gene sequence database D
    >> output: All genes g in D that are homologs of S
    """
    homologs = []

    m = len(S) + 1
    n = len(D) + 1
    dot_plot_matrix = init_matrix(m, n)

    for i in range(1, m):
        for j in range(1, n):
            if S[i - 1] == D[j - 1]:
                eyeballing(dot_plot_matrix, i, j)
    return dot_plot_matrix


def eyeballing(matrix, i, j):
    """This could result in lots of noice we're not interested in"""
    matrix[i][j] = True


def kmer(matrix, i, j, k):
    """Now we need substrings to be at least of size k"""
    raise NotImplementedError()