def confusion_matrix(tp, tn, fp, fn):
    pass


def roc(pattern: str, n: int = 5):
    pat_l = len(pattern)
    positive_current_count = 0
    positive_list = []

    for elem in pattern:
        if len(positive_list) == n:
            break

        if elem == "P":
            positive_current_count += 1
        elif elem == "N":
            positive_list.append(positive_current_count)

    return 1 / (n * pat_l) * sum(positive_list)