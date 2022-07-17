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
        self.play(Write(radius), Write(l_label))

        circle = Circle(radius=radius.get_length(), color=WHITE)
        circle.move_to(dot1.get_center())
        self.play(Write(circle))

        dot_lambda = Dot(point=([-1.5, 0.5, 0]), color=BLUE)
        dot_lambda_label = MathTex(r"\lambda").next_to(dot_lambda, DOWN).scale(0.7)
        self.play(Write(dot_lambda), Write(dot_lambda_label))

