from lcs import lcs
import pandas as pd


def read_from_file(filename):
    df = pd.read_csv(filename, delimiter="\n")
    return df


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


def main():
    s1, s2 = ask_for_files()
    check_lcs(s1, s2)
