from manim import *


class GDisk(Scene):
    def construct(self):
        title = Text("Gershgorin's Theorem", font_size=60).shift(3*UP)
        self.play(Write(title))

        thm1 = Tex(r"(1): $\forall A\in M_n$", r", ", r"$\sigma(A) \subseteq G(A)$").shift(UP)
        thm2 = Tex(r"(2): Further, if there is a connected component of $G(A)$ \\ with k disks, then there contain exactly k eigenvalues.")
        self.play(Write(thm1))
        self.wait(2)
        self.play(Write(thm2))
