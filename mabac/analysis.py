from pymabac.tests.mabac_model import MABAC
from metrics import weighted_rank_difference, spearman_correlation
import numpy as np

def sensitivity_analysis(reference, matrix, weights, types):
    rank_list, rw_list, spearman_list = [], [], []
    for j in range(matrix.shape[1]):
        reduced_matrix = np.delete(matrix, j, axis=1)
        reduced_weights = np.delete(weights, j)
        reduced_types = np.delete(types, j)

        model = MABAC(reduced_matrix, reduced_weights, reduced_types)
        alt_ranking = model.run()

        rank_list.append(alt_ranking)
        rw_list.append(weighted_rank_difference(reference, alt_ranking))
        spearman_list.append(spearman_correlation(reference, alt_ranking))
    return rank_list, rw_list, spearman_list
