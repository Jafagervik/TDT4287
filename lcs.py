def lcs(A: str, B: str) -> int:
    """Returns longest common subsequence between two strings."""
    m = len(A) + 1
    n = len(B) + 1
    memo = [[0] * (n) for i in range(m)]

    for row in range(1, m):
        for col in range(1, n):
            if A[row - 1] == B[col - 1]:
                memo[row][col] = 1 + memo[row - 1][col - 1]
            else:
                memo[row][col] = max(memo[row - 1][col], memo[row][col - 1])
    return memo, memo[m - 1][n - 1]


def print_lcs(a, S, i, j):
    """Prints the longest common subsequence."""
    if i == 0 or j == 0:
        return

    if a[i - 1][j] == a[i, j - 1]:
        print_lcs(a, S, i - 1, j)
    elif a[i][j] == a[i, j - 1]:
        print_lcs(a, S, i, j)
    else:
        print_lcs(a, S, i - 1, j - 1)
        print(S[i])
