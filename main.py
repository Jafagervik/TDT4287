from global_alignment import new_ga, traceback
from typing import Any
from lcs import lcs
from edit_distance import ed
from suffixtrie import SuffixTrie
import pandas as pd


def read_from_file(filename) -> Any:
    return pd.read_csv(filename, delimiter="\n")


def ask_for_files() -> tuple:
    f1 = input("Input name of first file: ")
    f2 = input("Input name of second file: ")
    string1 = read_from_file(f1)
    string2 = read_from_file(f2)
    return string1, string2


def check_lcs(string1: str, string2: str) -> int:
    print(
        f"The longest common substring between these two dna structures is of length {lcs(string1, string2)}"
    )


def check_ed(string1: str, string2: str) -> int:
    print(
        f"The edit distance between these two dna structures is of length {ed(string1, string2)}"
    )


def check_ga(string1: str, string2: str):
    print(f"traceback: {traceback(string1, string2, new_ga(string1, string2))}")


def check_suffix_trie(string1: str) -> None:
    trie = SuffixTrie(string1)
    print(trie.has_substring("ana"))


def main():
    # s1, s2 = ask_for_files()
    # check_lcs("ACGGTAC", "CTCGATC")
    # check_ed("CTCGACT", "CTTCGTC"
    check_ga("AGCT", "ATGCT")


if __name__ == "__main__":
    main()
