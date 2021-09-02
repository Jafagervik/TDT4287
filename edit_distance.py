def ed(A: str, B: str) -> int:
    """
    Returns the edit distance, or the cost of operations to transform A into B.
    Levenshtein distance is used to calculate our ED.
    """
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
            cost = 0 if A[r - 1] == B[c - 1] else 1
            memo[r][c] = min(
                memo[r - 1][c - 1] + cost, memo[r - 1][c] + 1, memo[r][c - 1] + 1
            )
    return memo, memo[m - 1][n - 1]
