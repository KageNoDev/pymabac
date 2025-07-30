import numpy as np

def weighted_rank_difference(r1, r2) -> float:
    N = len(r1)
    a, b = np.array(r1), np.array(r2)
    weights = (N - a + 1) + (N - b + 1)
    numerator = np.sum((a - b) ** 2 * weights)
    denominator = N ** 4 + N ** 3 - N ** 2 - N
    return 1 - (6 * numerator) / denominator

def spearman_correlation(r1, r2) -> float:
    n = len(r1)
    rank1 = np.argsort(np.argsort(r1)) + 1
    rank2 = np.argsort(np.argsort(r2)) + 1
    d_squared = np.sum((rank1 - rank2) ** 2)
    return 1 - (6 * d_squared) / (n * (n**2 - 1))
