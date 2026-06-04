import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        #value = []
        #for i in range(len())
        result = 1 / (1 + np.exp(-z))
        return np.round(result, 5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        value = []
        for i in range(len(z)):
            result = max(0, z[i])
            value.append(float(result))
        return value
