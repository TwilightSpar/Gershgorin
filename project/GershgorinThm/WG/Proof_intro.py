from manim import *


class Proof_intro(Scene):
    def construct(self):
        title = Text("Proof of Gershgorin's Theorem (1)", font_size=50).shift(UP*2.5)
        self.play(Write(title))

        thm1 = Tex(r"(1): $\forall A\in M_n$", r", ", r"$\sigma(A) \subseteq G(A)$")
        self.play(Write(thm1))