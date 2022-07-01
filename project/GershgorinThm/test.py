import numpy as np
from numpy import linalg as LA

w, v = LA.eig(np.array(
    [[1, 0, 5.1],
     [-2.6, 3 + 3j, 0],
     [0, -3.5, 5 + 1j]]
))
print(w)
