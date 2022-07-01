import numpy as np
from manim import *


def updated_matrix(matrix, d):
    change = np.round(d.get_value(), 4)
    matrix = np.array(matrix)
    addition = np.array(
        [[0, 0, -change],
         [0, change, 0],
         [change, 0, 0]]
    )

    return (matrix + addition).tolist()


def matrix_tex(matrix):
    s = r'$\begin{pmatrix} '
    for row in matrix:
        for col in row:
            s += str(np.round(col, 2)).strip('()') + ' & '
        s = s[0:-3] + r' \\ '
    s = s[0:-3]
    s += r" \end{pmatrix}$"
    s = s.replace('1j', 'j').replace('+1j', '+j')
    return Tex(s)
