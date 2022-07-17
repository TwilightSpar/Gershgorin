from manim import *


class Proof1(Scene):
    def construct(self):

        Formula_1 = MathTex(r"Ax=\lambda x,\forall \lambda").align_on_border(UP)
        Formula_2 = MathTex(r"Define \quad k=\arg\max_i |x_i|").next_to(Formula_1, DOWN)
        #圈出最大行
        Formula_2_1 = MathTex(r"\mbox{Example } x = ").next_to(Formula_2, DOWN)
        Formula_2_2 = MathTex(r"= \lambda \begin{bmatrix} 1\\ i \\ 2+i \end{bmatrix}")
        Formula_4_1 = MathTex(r"\sum_j", r"a_{kj}x_j", r"=", r"\lambda x_k")
        Formula_4_2 = MathTex(r"\lambda x_k", r"=", r"\sum_j", r"a_{kj}x_j")
        matrix_X1 = Matrix([[1], ["i"], ["2+i"]], element_alignment_corner=DOWN)
        matrix_X2 = Matrix([[1], ["i"], ["2+i"]], element_alignment_corner=DOWN)
        MGroup = VGroup(Formula_2_1, matrix_X1).arrange_in_grid(cols=2)

        rect_1 = SurroundingRectangle(matrix_X1.get_rows()[2])
        tex1 = MathTex(r"k = 3", color=YELLOW).scale(0.7).next_to(rect_1, RIGHT * 1.5)

        self.play(Write(Formula_1))
        self.wait()

        self.play(Write(Formula_2))
        self.wait()

        self.play(Write(MGroup))
        self.wait()
        self.play(Create(rect_1))
        self.wait()
        self.play(Write(tex1))
        self.wait(3)

        self.remove(MGroup, rect_1, tex1)

        self.play(Formula_2.animate.align_on_border(UP), Formula_1.animate.move_to([0, 0, 0]),run_time = 2)
        self.play(Formula_2.animate.set_fill(opacity=0.5))
        self.wait()

        Formula_3 = MathTex(r" = \lambda ")
        matrix_A = Matrix([["a_{11}", "...", "a_{1n}"], ["...", "...", "..."], ["a_{k1}", "...", "a_{kn}"], ["...", "...", "..."], ["a_{n1}", "...", "a_{nn}"]], element_alignment_corner=DOWN)
        matrix_X_1 = Matrix([["x_1"], ["..."], ["x_k"], ["..."], ["x_n"]], element_alignment_corner=DOWN)
        matrix_X_2 = Matrix([["x_1"], ["..."], ["x_k"], ["..."], ["x_n"]], element_alignment_corner=DOWN)
        MGroup2 = VGroup(matrix_A, matrix_X_1, Formula_3, matrix_X_2).arrange_in_grid(cols=4)

        rect_2 = SurroundingRectangle(matrix_A.get_rows()[2])
        rect_3 = SurroundingRectangle(matrix_X_1.get_columns()[0])
        rect_4 = SurroundingRectangle(matrix_X_2.get_rows()[2])

        self.play(ReplacementTransform(Formula_1, MGroup2))
        self.wait(3)
        self.play(Create(rect_2))
        self.play(Create(rect_3))
        self.play(Create(rect_4))
        self.wait(3)

        self.play(Uncreate(rect_2), Uncreate(rect_3), Uncreate(rect_4))

        self.play(ReplacementTransform(MGroup2, Formula_4_1))
        self.wait()
        self.play(TransformMatchingTex(Formula_4_1, Formula_4_2))
        self.wait()
#manim -pql Proof1.py Proof1
