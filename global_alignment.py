GAP_INTRODUCTION_PENALTY = 2  # p
GAP_EXTENSION_PENALTY = 1  # sigma

PENALTY = -(GAP_INTRODUCTION_PENALTY + GAP_EXTENSION_PENALTY)


def dna(r: chr, s: chr) -> int:
    if r == s:
        return 1
    if r == "-" or s == "-":
        return GAP_INTRODUCTION_PENALTY
    if r != s:
        return GAP_EXTENSION_PENALTY


def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()


"""
def ga(A: str, B: str) -> int:
    #Finds the best alignment between S and R given scoring function
    m = len(A) + 1
    n = len(B) + 1
    memo = [[0] * (n) for i in range(m)]

    # Initialize memo
    for r in range(m):
        memo[r][0] = r
    for c in range(n):
        memo[0][c] = c

    for r in range(1, m):
        for c in range(1, n):
            memo[r][c] = max(
                memo[r - 1][c - 1] + dna(A[r], B[c]),
                memo[r - 1][c] + dna("-", B[c]),
                memo[r][c - 1] + dna(A[r], "-"),
            )
    print(memo)
    return memo[m - 1][n - 1]

print(ga("AGCTTAGC", "GCTAGGA"))
"""


def init_matrix(m: int, n: int):
    memo = [[0] * (n) for i in range(m)]

    # Initialize memo
    for r in range(m):
        memo[r][0] = r
    for c in range(1, n):
        memo[0][c] = c

    return memo


def global_alignment_affine_gaps(S: str, R: str):
    """Returns

    Time Complexity = O(m*n*max*3)
    Space Complexity = O(3 * m * n)
    """

    m = len(S) + 1
    n = len(R) + 1

    ga = init_matrix(m, n)
    ga_insert = init_matrix(m, n)
    ga_delete = init_matrix(m, n)

    for i in range(1, m):
        for j in range(1, n):
            ga_insert[i][j] = max(
                ga_insert[i - 1][j] - GAP_EXTENSION_PENALTY,
                ga[i - 1][j] + PENALTY,
            )
            ga_delete[i][j] = max(
                ga_delete[i][j - 1] - GAP_EXTENSION_PENALTY,
                ga[i][j - 1] + PENALTY,
            )

            cost = -1 if S[i - 1] != R[j - 1] else 0
            ga[i][j] = max(
                ga[i - 1][j - 1] + cost,
                ga_insert[i][j],
                ga_delete[i][j],
            )

    print_matrix(ga)
    return ga