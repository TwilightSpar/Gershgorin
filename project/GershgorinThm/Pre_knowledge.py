from manim import *


class GDisk(Scene):
    def construct(self):
        tex1 = Tex("Pre-knowledge", color=YELLOW).to_edge(UP)
        tex2 = Tex("Basics about complex number and complex plane").shift(2*UP)
        tex3 = Tex("Basics about matrix and eigenvalue").shift(DOWN)
        plane = ComplexPlane(
            x_range=[-1, 5],
            y_range=[-1, 2.5]
        ).add_coordinates().scale(0.5).next_to(tex2, DOWN)

        matrix_object = Matrix([[2j, 1], [3.14, 2j]],
                               bracket_h_buff=SMALL_BUFF,
                               bracket_v_buff=SMALL_BUFF,
                               left_bracket="(",
                               right_bracket=")").scale(0.8).next_to(tex3, DOWN)

        self.add(tex1)
        self.play(Write(tex2))
        self.play(Create(plane))
        self.play(Write(tex3))
        self.play(Create(matrix_object))
