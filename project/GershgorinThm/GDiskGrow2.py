from manim import *
from numpy import linalg as LA
import numpy as np
from Matrix_helper import *


class GDisk(Scene):
    def construct(self):
        def matrix_tex_updater(matrix, d):
            matrix = gdisk_growing_updater(matrix, d)
            return matrix_tex(matrix).scale(0.75).move_to(3 * RIGHT)

        def gdisk_growing_updater(matrix, d):
            change = d.get_value()
            matrix = np.array(matrix)
            addition = np.array(
                [[0, 1j, 0.5],
                 [1, 0, 0.5],
                 [1.5, 0.2, 0]]
            ) * change
            return (matrix + addition).tolist()

        def g_disk_circle_updater(matrix, i):
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

        def evalue_dot_updater(matrix, d, i):
            matrix = gdisk_growing_updater(matrix, d)
            w, v = LA.eig(np.array(matrix))
            return Dot(plane.n2p(w[i]), color=BLUE)

        # display complex plane
        plane = ComplexPlane(
            x_range=[-1, 5.5],
            y_range=[-1, 2.5]
        ).add_coordinates().align_on_border([-1, 0, 0])

        delta = ValueTracker(0)
        matrix_content = [[1j, 0, 0],
                          [0, 3 + 0.5j, 0],
                          [0, 0, 4]]

        matrix_tex_object = matrix_tex(matrix_content)
        matrix_tex_object.add_updater(
            lambda mob: mob.become(matrix_tex_updater(matrix_content, delta))
        )

        disk_group = Group(plane, matrix_tex_object)
        epsilon_Tex = MathTex(r"\epsilon: 0 \to 1 \\ A_{\epsilon}= ").next_to(matrix_tex_object, UP).shift(RIGHT * 3)
        disk_group.add(epsilon_Tex)

        for i in range(len(matrix_content)):
            c = g_disk_circle_updater(matrix_content, i)
            c.add_updater(
                lambda mob, i=i: mob.become(g_disk_circle_updater(gdisk_growing_updater(matrix_content, delta), i))
            )
            disk_group.add(c)

        w, v = LA.eig(np.array(matrix_content))

        for i in range(len(w)):
            evalue_point = Dot(plane.n2p(w[i]), color=BLUE)
            evalue_point.add_updater(
                lambda mob, i=i: mob.become(evalue_dot_updater(matrix_content, delta, i))
            )
            disk_group.add(evalue_point)

        # display ordinate and matrix
        self.add(disk_group)
        # grow matrix from 0 to 1
        self.play(delta.animate.set_value(1), run_time=7)
