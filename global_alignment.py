def dna(r, s):
    if r == s:
        return 1
    if r == "-" or s == "-":
        return "-q"
    if r != s:
        return "-y"


def ga(A: str, B: str) -> int:
    """Finds the best alignment between S and R given scoring function"""
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
            cost = 0 if A[r - 1] == B[c - 1] else -1
            memo[r][c] = max(
                memo[r - 1][c - 1] + dna(A[r], B[c]),
                memo[r - 1][c] + dna("-", B[c]),
                memo[r][c - 1] + dna(A[r], "-"),
            )
    print(memo)
    return memo[m - 1][n - 1]


print(ga("AGCTTAGC", "GCTAGGA"))
