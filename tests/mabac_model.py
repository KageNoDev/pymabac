import numpy as np

class MABAC:
    def __init__(self, decision_matrix: np.ndarray, weights: np.ndarray, types: np.ndarray):
        self.decision_matrix = decision_matrix
        self.weights = weights
        self.types = types

    def normalize(self) -> np.ndarray:
        norm_matrix = self.decision_matrix.astype(float).copy()
        for i in range(self.decision_matrix.shape[1]):
            col = self.decision_matrix[:, i]
            if self.types[i] == 0:
                norm_matrix[:, i] = (np.max(col) - col) / (np.max(col) - np.min(col))
            else:
                norm_matrix[:, i] = (col - np.min(col)) / (np.max(col) - np.min(col))
        return norm_matrix

    def weighted_matrix(self, norm_matrix: np.ndarray) -> np.ndarray:
        return norm_matrix * self.weights

    def border_field(self, weighted_matrix: np.ndarray) -> float:
        return np.prod(weighted_matrix) ** (1 / self.decision_matrix.shape[0])

    def distance_field(self, weighted_matrix: np.ndarray, G: float) -> np.ndarray:
        return weighted_matrix - G

    def alternative_assessment(self, Q: np.ndarray) -> np.ndarray:
        return np.sum(Q, axis=1)

    def run(self) -> np.ndarray:
        norm = self.normalize()
        weighted = self.weighted_matrix(norm)
        G = self.border_field(weighted)
        Q = self.distance_field(weighted, G)
        S = self.alternative_assessment(Q)
        return np.argsort(np.argsort(S)) + 1
