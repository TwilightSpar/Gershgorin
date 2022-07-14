from manim import *


class matrix(Scene):
    def construct(self):
        Formula_1_1 = MathTex(r"A")
        Formula_1_2 = MathTex(r"x")
        Formula_1_3 = MathTex(r"= \lambda")
        Formula_1_4 = MathTex(r"x")
        TGroup = VGroup(Formula_1_1, Formula_1_2, Formula_1_3, Formula_1_4).arrange_in_grid(cols=4, buff=0.2)

        Formula_2_1 = MathTex(r"A")
        Formula_2_2 = MathTex(r"= \lambda")

        matrix_X1 = Matrix([["a_{11}", "...", "a_{1n}"], ["...", "~", "..."], ["a_{k1}", "...", "a_{kn}"], ["...", "~", "..."], ["a_{n1}", "...", "a_{nn}"]], element_alignment_corner=DOWN)
        matrix_X2 = Matrix([[1], ["i"], ["2+i"]], element_alignment_corner=DOWN)
        MGroup = VGroup(Formula_2_1, matrix_X1, Formula_2_2, matrix_X2).arrange_in_grid(cols=4)

        self.play(Write(TGroup))
        self.wait()
        self.play(ReplacementTransform(TGroup, MGroup))
        self.wait()
        self.play(Create(SurroundingRectangle(matrix_X1.get_rows()[2])))