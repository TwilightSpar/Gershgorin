from manim import *


class Proof1(Scene):
    def construct(self):
        title = Tex("Proof of Thm").shift(UP * 3.5)
        Formula_1 = MathTex(r"Ax=\lambda x,\forall \lambda").shift(UP * 2.5)
        Formula_2 = MathTex(r"Define \quad k=\arg\max_i |x_i|").next_to(Formula_1, DOWN)
        #圈出最大行
        Formula_2_1 = MathTex(r"\mbox{Example } x = \begin{bmatrix} 1\\ i \\ 2+i \end{bmatrix}, A").next_to(Formula_2, DOWN)
        Formula_2_2 = MathTex(r"= \lambda \begin{bmatrix} 1\\ i \\ 2+i \end{bmatrix}")
        matrix_X1 = Matrix([[1], ["i"], ["2+i"]], element_alignment_corner=DOWN)
        matrix_X2 = Matrix([[1], ["i"], ["2+i"]], element_alignment_corner=DOWN)
        MGroup = VGroup(Formula_2_1, matrix_X1, Formula_2_2).arrange_in_grid(cols=4)

        rect = SurroundingRectangle(matrix_X1.get_rows()[2])
        tex1 = MathTex(r"k = 3", color=YELLOW).scale(0.7).next_to(rect, DOWN)
        self.play(Write(title))

        self.play(Write(Formula_1))
        self.wait()

        self.play(Write(Formula_2))
        self.wait()

        self.play(Write(MGroup))
        self.wait()
        self.play(Create(rect))
        self.wait()
        self.play(Write(tex1))
        self.wait()

        self.remove(MGroup)

        self.remove(Formula_1)
        self.play(Formula_2.animate.next_to(title, DOWN))
        self.play(Write(Formula_1.next_to(Formula_2, DOWN)))
        self.wait()

        Formula_3 = MathTex(r" = \lambda ")
        matrix_A = Matrix([["a_{11}", "...", "a_{1n}"], ["...", "...", "..."], ["a_{k1}", "...", "a_{kn}"], ["...", "...", "..."], ["a_{n1}", "...", "a_{nn}"]], element_alignment_corner=DOWN)
        matrix_X_1 = Matrix([["x_1"], ["..."], ["x_k"], ["..."], ["x_n"]], element_alignment_corner=DOWN)
        matrix_X_2 = Matrix([["x_1"], ["..."], ["x_k"], ["..."], ["x_n"]], element_alignment_corner=DOWN)
        MGroup2 = VGroup(matrix_A, matrix_X_1, Formula_3, matrix_X_2).arrange_in_grid(cols=4)
        self.play(ReplacementTransform(Formula_1, MGroup2))
        self.wait()
        self.play(Create(SurroundingRectangle(matrix_A.get_rows()[2])))
        self.play(Create(SurroundingRectangle(matrix_X_1.get_rows()[2])))
#manim -pql Proof1.py Proof1
