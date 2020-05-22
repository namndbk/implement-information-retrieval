import numpy as np


def cosin(v1, v2):
    return np.dot(v1, v2) / np.sqrt(np.sum(v1**2) * np.sum(v2**2))


def euclidean(v1, v2):
    return np.sqrt(np.sum((v1 - v2)**2))


def manhattan(v1, v2):
    return np.sum(np.absolute(v1 - v2))


if __name__=="__main__":
    v1 = np.array([1, 2, 3])
    v2 = np.array([1, 2, 3])
    print(cosin(v1, v2))
    print(euclidean(v1, v2))
    print(manhattan(v1, v2))