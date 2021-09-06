import numpy as np

GAP_INTRODUCTION_PENALTY = 2  # p
GAP_EXTENSION_PENALTY = 1  # sigma


def init_matrix(m: int, n: int):
    return [[0] * (n) for i in range(m)]


def dna(r: chr, s: chr) -> int:
    if r == s:
        return 1
    if r == "-" or s == "-":
        return GAP_INTRODUCTION_PENALTY
    if r != s:
        return GAP_EXTENSION_PENALTY


def la(S: str, R: str):
    m = len(S) + 1
    n = len(R) + 1
    la_mat = init_matrix(m, n)
    index_max = (1, 2)

    for i in range(1, m):
        for j in range(1, n):
            la_mat[i][j] = max(
                la_mat[i - 1][j] + dna(S[i - 1], "-"),
                la_mat[i][j - 1] + dna("-", R[j - 1]),
                la_mat[i - 1][j - 1] + dna(S[i - 1], R[j - 1]),
                0,
            )

    print(la_mat)
    return la_mat, index_max


def backtrack_la(mat, index_pair):
    root = mat[index_pair[0]][index_pair[1]]
