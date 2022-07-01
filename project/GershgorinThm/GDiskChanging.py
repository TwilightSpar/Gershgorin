from manim import *
from numpy import linalg as LA
import numpy as np


class GDisk(Scene):
    def construct(self):
        plane = ComplexPlane(
            x_range=[-1, 5],
            y_range=[-2, 3]
        ).add_coordinates()

        delta = ComplexValueTracker(0+0j)
        matrix_content = [[2+1j, 1j, 1],
                          [0.25, 3, 0.5],
                          [0, 0, 4]]

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

        def change_matrix(matrix, d):
            change = np.round(d.get_value(), 2)
            matrix = np.array(matrix)
            addition = np.array(
                [[0, 0, -change],
                 [0, change, 0],
                 [change, 0, 0]]
            )

            matrix = (matrix + addition).tolist()
            return matrix_tex(matrix)

        matrix_tex_object = matrix_tex(matrix_content).scale(0.5)
        matrix_tex_object.add_updater(
            lambda mob: mob.become(change_matrix(matrix_content, delta))
        )

        # display ordinate and matrix
        g = VGroup(plane, matrix_tex_object).arrange(buff=1.0)
        self.add(g)


        # def i_th_g_disk(matrix, i):
        #     center = matrix[i][i]
        #     center_point = Dot(plane.n2p(center), color=YELLOW)
        #
        #     r = 0
        #     for index in range(len(matrix[i])):
        #         if index == i:
        #             continue
        #         module = abs(matrix[i][index])
        #         r += module
        #
        #     if r == 0:
        #         circle = Dot(color=RED)
        #         circle.move_to(center_point)
        #     else:
        #         circle = Circle(radius=r)
        #         circle.move_to(center_point)
        #
        #     return circle
        #
        # for i in range(len(matrix_content)):
        #     c = i_th_g_disk(matrix_content, i)
        #     disk_group.add(c)
        #     self.add(c)

        self.play(delta.animate.set_value(0.5+0.3j), run_time=4)
        # self.wait(2)

        # w, v = LA.eig(np.array(self.matrix_content))
        # w = np.round(w, 2)
        # evalue_text = Text("Eigenvalues are: " + np.array2string(w, separator=', ')).next_to(disk_group, UP).scale(0.7)
        # self.play(Write(evalue_text))
        # self.remove(*self.mobjects)
        # self.add(disk_group, evalue_text)
        #
        # self.wait(2)
        # for e in w:
        #     evalue_point = Dot(plane.n2p(e), color=BLUE)
        #     self.add(evalue_point)
        #
        # self.remove(evalue_text)
        # self.wait(3)
