import numpy as np
def get_data(N=1000):
    x1 = np.random.normal(0, 1, N)
    x2 = np.random.normal(5, 3, N)
    x3 = x1 * 3 + np.random.normal(0, 2, N)
    return x1, x2, x3