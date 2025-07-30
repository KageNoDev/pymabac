import numpy as np
from mabac import MABAC, weighted_rank_difference, spearman_correlation, sensitivity_analysis

def test_mabac_ranking():
    matrix = np.array([
        [3, 4, 2],
        [2, 5, 3],
        [4, 3, 1]
    ])
    weights = np.array([0.3, 0.4, 0.3])
    types = np.array([1, 1, 0])

    model = MABAC(matrix, weights, types)
    ranking = model.run()

    assert len(ranking) == 3
    assert set(ranking) == {1, 2, 3}

def test_metrics():
    r1 = [1, 2, 3]
    r2 = [3, 1, 2]

    assert 0 <= weighted_rank_difference(r1, r2) <= 1
    assert -1 <= spearman_correlation(r1, r2) <= 1

def test_sensitivity_analysis():
    matrix = np.array([
        [3, 4, 2],
        [2, 5, 3],
        [4, 3, 1]
    ])
    weights = np.array([0.3, 0.4, 0.3])
    types = np.array([1, 1, 0])
    model = MABAC(matrix, weights, types)
    ref = model.run()

    ranks, rws, corrs = sensitivity_analysis(ref, matrix, weights, types)

    assert len(ranks) == 3
    assert len(rws) == 3
    assert len(corrs) == 3
