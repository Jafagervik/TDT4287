def knut_morris_plot(T: str, P: str) -> tuple(list[int], int):
    """Substring search algorithm O(m+n)"""

    # longest prefix sufffix

    m = len(T)
    n = len(P)

    lps = [0] * n
    j = 0

    compute_lcs_array(P, n, lps)

    i = 0
    while i < n:
        if P[j] == T[i]:
            i += 1
            j += 1

            # If we're at end
            if j == n:
                print(f"Found pattern at index {str(i-j)}")
                j = lps[j - 1]

        elif i < m and P[j] != T[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def compute_lcs_array(P, n, lps):
    # length of the previous longest prefix suffix
    l = 0

    lps[0] = 0
    i = 1

    while i < n:
        if P[i] == P[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1
