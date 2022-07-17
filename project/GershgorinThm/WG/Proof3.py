from manim import *


class Proof3(Scene):
    def construct(self):
        Formula_13 = MathTex(r"|\lambda-a_{kk}|", r"\le", r"\sum_{j\ne k} |a_{kj}|").align_on_border(UP)
        dot1 = Dot(point=([0, -1, 0]), color=BLUE)
        dot2 = Dot(point=([2.5, -1, 0]), color=BLUE)
        center_label = MathTex(r"a_{kk}").next_to(dot1, LEFT).scale(0.7)
        radius = Line(dot1.get_center(), dot2.get_center(), color=YELLOW)
        l_label = MathTex(r"\sum_{j\ne k} |a_{kj}|").next_to(radius, DOWN).scale(0.7)

        self.add(Formula_13)
        self.wait()
        self.play(Create(dot1))
        self.play(Write(center_label))
        self.wait()
        self.play(Create(radius), Create(l_label))
        self.wait(2)

        circle = Circle(radius=radius.get_length(), color=WHITE)
        circle.move_to(dot1.get_center())
        self.play(Create(circle))
        self.wait(2)

        dot_lambda = Dot(point=([-1.3, 0.5, 0]), color=BLUE)
        dot_lambda_label = MathTex(r"\lambda").next_to(dot_lambda, DOWN).scale(0.7)
        self.play(Create(dot_lambda))
        self.play(Write(dot_lambda_label))

        module_of_lambda = DashedLine(start = dot_lambda.get_center(), end= dot1.get_center())
        self.play(Create(module_of_lambda))
        self.wait(3)

        Formula_14 = MathTex(r"|\lambda-a_{kk}|", r"\le", r"\sum_{j\ne k} |a_{kj}|", r"; \ \forall \lambda").align_on_border(UP).scale(0.8)
        self.play(TransformMatchingTex(Formula_13, Formula_14))
        self.wait(2)
        Formula_15 = MathTex(r"|\lambda-a_{kk}|", r"\le", r"\sum_{j\ne k} |a_{kj}|", r"; \ \forall \lambda", r"\Leftrightarrow", r"\sigma(A) \subseteq G(A)").align_on_border(UP).scale(0.8)
        self.play(TransformMatchingTex(Formula_14, Formula_15))
