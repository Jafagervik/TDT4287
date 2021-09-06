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
            memo[r][c] = max(
                memo[r - 1][c - 1] + dna(A[r], B[c]),
                memo[r - 1][c] + dna("-", B[c]),
                memo[r][c - 1] + dna(A[r], "-"),
            )
    print(memo)
    return memo[m - 1][n - 1]


def new_ga(A: str, B: str, gap_penalty: int = -2, mismatch: int = -1, match: int = 1):
    m = len(A) + 1
    n = len(B) + 1

    memo = [[0] * (n) for i in range(m)]

    # Initialize memo
    for r in range(m):
        memo[r][0] = r * gap_penalty
    for c in range(n):
        memo[0][c] = c * gap_penalty

    for i in range(1, m):
        for j in range(1, n):
            cost = match if A[i - 1] == B[j - 1] else mismatch
            memo[i][j] = max(
                memo[i - 1][j - 1] + cost,
                memo[i][j - 1] + gap_penalty,
                memo[i - 1][j] + gap_penalty,
            )

    return memo


def traceback(A: str, B: str, memo):
    m = len(A) + 1
    n = len(B) + 1

    i = m - 1
    j = n - 1
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            print("\\")
            i -= 1
            j -= 1
        elif memo[i][j - 1] > memo[i - 1][j]:
            print("--")
            j -= 1
        else:
            print("|")
            i -= 1

    if i == 0:
        for a in range(j):
            print("--")
    if j == 0:
        for a in range(i):
            print("|") * i
