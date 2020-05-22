import numpy as np

def levenshtein(x, y) -> int:
    """
    :param x: string
    :param y: string
    :return: levenshtein distance(x, y) -> int
    """
    n = len(x)
    m = len(y)
    d = np.zeros((n+1, m+1), dtype=int)
    for i in range(n+1):
        d[i, 0] = i
    for j in range(m+1):
        d[0, j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:f
                cost = 0
            else:
                cost = 1
            d[i, j] = min(d[i-1, j] + 1, d[i, j-1] + 1, d[i-1, j-1] + cost)
    return d[n, m]
import math
if __name__ == '__main__':
    print(levenshtein("nation", "national"))
