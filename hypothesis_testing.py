from .local_alignment import la
import random

""" How to Randomize?

Universal
    - Letter distribution from database
Global
    - Letter distribution from similar sequences
Local
    - Letter distribution from Q and D
    - Shuffle whole D
    - Shuffle regions of D with similar sequence composition


"""


def randomization(Q: str, D: str, iterations: int = 10000):
    """Randomized-based hhypothesis testing. Check if any random string from database is bigger than D with LA algorithm."""
    x = la(Q, D)
    count = 0
    for i in range(iterations):
        if la(Q, random.rand(D)) >= x:
            count += 1
    return (count + 1) / (iterations + 1)
