from manim import *
from numpy import linalg as LA
import numpy as np


class GDisk(Scene):
    matrix_content = [[2. + 1.j, 1.j, 1],
                      [0.25, 3., 0.5],
                      [0., 0., 4]]

    def construct(self):
        matrix_object = Matrix(self.matrix_content,
                               bracket_h_buff=SMALL_BUFF,
                               bracket_v_buff=SMALL_BUFF,
                               left_bracket="(",
                               right_bracket=")")

        plane = ComplexPlane(
            x_range=[-1, 5],
            y_range=[-1, 2.5]
        ).add_coordinates()
        # display ordinate and matrix
        disk_group = Group(plane, matrix_object).arrange_in_grid(buff=0.5)
        self.add(disk_group)

        def i_th_g_disk(matrix, i):
            center = matrix[i][i]
            center_point = Dot(plane.n2p(center), color=YELLOW)
            center_label = MathTex((center.real, center.imag)).next_to(center_point, UP, 0.03).scale(0.5)

            group = Group(center_point, center_label)

            disk_center_rectangle = SurroundingRectangle(matrix_object.get_rows()[i][i])
            # center entry, and center point
            self.play(Create(disk_center_rectangle))
            self.add(group)
            self.wait(2)

            r = 0
            d1 = Dot(color=BLUE).next_to(matrix_object, UP)
            d2 = Dot(d1.get_center(), color=BLUE)
            r_line = Line(d1.get_center(), d2.get_center())
            r_line.add_updater(lambda z: z.become(Line(d1.get_center(), d2.get_center())))
            self.add(d1, d2, r_line)

            for index in range(len(matrix[i])):
                if index == i:
                    continue
                module = abs(matrix[i][index])
                r += module
                rectangle = SurroundingRectangle(matrix_object.get_rows()[i][index], color=BLUE)
                self.play(Create(rectangle))
                self.play(d2.animate.shift(module * RIGHT))
                self.remove(rectangle)

            self.wait()
            self.remove(d1, d2)
            r_line.clear_updaters()

            if r == 0:
                circle = Dot(color=RED)
                circle.move_to(center_point)
            else:
                circle = Circle(radius=r)
                circle.move_to(center_point)
                self.play(r_line.animate.shift(center_point.get_center() - d1.get_center()))

            self.play(Create(circle))
            self.play(FadeOut(disk_center_rectangle, r_line))
            self.wait(2)
            return circle

        for i in range(len(self.matrix_content)):
            c = i_th_g_disk(self.matrix_content, i)
            disk_group.add(c)

        self.wait(2)

        w, v = LA.eig(np.array(self.matrix_content))
        w = np.round(w, 2)
        evalue_text = Text("Eigenvalues are: "+np.array2string(w, separator=', ')).next_to(disk_group, UP).scale(0.7)
        self.play(Write(evalue_text))
        self.remove(*self.mobjects)
        self.add(disk_group, evalue_text)

        self.wait(2)
        for e in w:
            evalue_point = Dot(plane.n2p(e), color=BLUE)
            self.play(FadeIn(evalue_point))
            self.play(Write(MathTex((e.real, e.imag)).next_to(evalue_point, UP, 0.03).scale(0.5)))

        self.remove(evalue_text)
        self.wait(3)
