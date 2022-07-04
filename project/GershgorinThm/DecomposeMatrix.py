from manim import *
from Matrix_helper import *


class GDisk(Scene):
    def construct(self):
        N = [[0, 1j, 0.5],
             [1, 0, 0.5],
             [1.5, 0.2, 0]]

        D = [[1j, 0, 0],
             [0, 3 + 0.5j, 0],
             [0, 0, 4]]

        A = [[1j, 1j, 0.5],
             [1, 3 + 0.5j, 0.5],
             [1.5, 0.2, 4]]

        A_tex = matrix_tex(A).tex_strings[0].strip("$")
        N_tex = matrix_tex(N).tex_strings[0].strip("$")
        D_tex = matrix_tex(D).tex_strings[0].strip("$")

        Eq1 = MathTex(r"A = ", A_tex)
        self.play(Write(Eq1))
        self.wait(2)

        Eq2 = MathTex(r"A = ", D_tex, " + ", N_tex)
        self.play(TransformMatchingTex(Eq1, Eq2), run_time=2)

        Eq3 = MathTex(r"D = ", D_tex).shift(UP * 2)
        Eq4 = MathTex(r"N = ", N_tex).shift(UP * 2)
        g = Group(Eq3, Eq4).arrange_in_grid(buff=0.5)
        self.play(FadeIn(g))
        self.wait(2)
        self.remove(g)

        Eq5 = MathTex(r"A = ", "D", " + ", "N")
        self.play(TransformMatchingTex(Eq2, Eq5), run_time=2)

        A_e = MathTex(r"A_{\epsilon} = ", "D", " + ", r"\epsilon", "N")
        self.play(TransformMatchingTex(Eq5, A_e))
        self.play(A_e.animate.shift(UP))
        self.wait(2)

        A_0 = MathTex(r"A_{0} = ", "D", " + ", r"0 * ", "N", "=", " D")
        self.play(Write(A_0))
        self.wait(2)

        A_1 = MathTex(r"A_{1} = ", "D", " + ", "N", "=", "A")
        self.play(TransformMatchingTex(A_0, A_1))
        self.wait(2)
