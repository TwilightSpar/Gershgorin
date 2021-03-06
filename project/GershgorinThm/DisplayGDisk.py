from manim import *
from numpy import linalg as LA
import numpy as np


class GDisk(Scene):
    matrix_content = [[1, 0, 5.1],
                      [-2.6, 3 + 3j, 0],
                      [0, -3.5, 5 + 1j]]

    def construct(self):
        matrix_object = Matrix(self.matrix_content,
                               h_buff=2.5,
                               bracket_h_buff=SMALL_BUFF,
                               bracket_v_buff=SMALL_BUFF,
                               left_bracket="(",
                               right_bracket=")")

        plane = ComplexPlane(
            x_range=[-5, 7.5],
            y_range=[-5, 5.5]
        ).add_coordinates()
        # display ordinate and matrix
        disk_group = Group(plane, matrix_object).arrange_in_grid(buff=0.5)
        self.add(disk_group)

        def i_th_g_disk(matrix, i):
            center = matrix[i][i]
            center_point = Dot(plane.n2p(center), color=YELLOW)

            r = 0

            for index in range(len(matrix[i])):
                if index == i:
                    continue
                module = abs(matrix[i][index])
                r += module

            if r == 0:
                circle = Dot(color=RED)
                circle.move_to(center_point)
            else:
                circle = Circle(radius=r)
                circle.move_to(center_point)

            return circle

        for i in range(len(self.matrix_content)):
            c = i_th_g_disk(self.matrix_content, i)
            disk_group.add(c)
            self.add(c)

        self.wait(2)

        w, v = LA.eig(np.array(self.matrix_content))
        w = np.round(w, 2)
        evalue_text = Text("Eigenvalues are: " + np.array2string(w, separator=', ')).next_to(disk_group, UP).scale(0.7)
        self.play(Write(evalue_text))
        self.remove(*self.mobjects)
        self.add(disk_group, evalue_text)

        self.wait(2)
        for e in w:
            evalue_point = Dot(plane.n2p(e), color=BLUE)
            self.add(evalue_point)

        self.remove(evalue_text)
        self.wait(3)
