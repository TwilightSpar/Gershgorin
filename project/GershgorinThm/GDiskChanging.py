from manim import *
from numpy import linalg as LA
import numpy as np
from Matrix_helper import *


class GDisk(Scene):
    def construct(self):
        def matrix_tex_updater(matrix, d):
            matrix = updated_matrix(matrix, d)
            return matrix_tex(matrix).scale(0.75).move_to(3*RIGHT)

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
            matrix = updated_matrix(matrix, d)
            w, v = LA.eig(np.array(matrix))
            return Dot(plane.n2p(w[i]), color=BLUE)

        # display complex plane
        plane = ComplexPlane(
            x_range=[-1, 5],
            y_range=[-2, 3]
        ).add_coordinates().align_on_border([-1, 0, 0])

        delta = ComplexValueTracker(0+0j)
        matrix_content = [[2+1j, 1j, 1],
                          [0.25, 3, 0.5],
                          [0, 0, 4]]

        matrix_tex_object = matrix_tex(matrix_content)
        matrix_tex_object.add_updater(
            lambda mob: mob.become(matrix_tex_updater(matrix_content, delta))
        )

        disk_group = Group(plane, matrix_tex_object)

        for i in range(len(matrix_content)):
            c = g_disk_circle_updater(matrix_content, i)
            c.add_updater(
                lambda mob, i=i: mob.become(g_disk_circle_updater(updated_matrix(matrix_content, delta), i))
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
        # change the matrix by a little value
        self.play(delta.animate.set_value(0.7 + 0.7j), run_time=5)
        self.play(delta.animate.set_value(-0.1 + 0.2j), run_time=5)
        self.play(delta.animate.set_value(0.5 + -0.7j), run_time=5)
        self.play(delta.animate.set_value(0 + 0.j), run_time=5)
