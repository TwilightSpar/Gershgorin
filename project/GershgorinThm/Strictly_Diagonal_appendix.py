from manim import *


class GDisk(Scene):
    def construct(self):
        plane = ComplexPlane(
            x_range=[-2, 2],
            y_range=[-2, 2]
        ).add_coordinates().shift(4*RIGHT)

        A = MathTex(
            r"\begin{pmatrix} 1+j & 0.2 & 0.2 \\ 0.2 & 2-j & 0.2 \\ 0.2 & 0.3 & -0.4-0.3j \end{pmatrix}").scale(0.6).shift(2.5 * LEFT)

        r1 = ValueTracker(0.4)
        r3 = ValueTracker(0.5)
        c1 = Dot(plane.n2p(1+1.j), color=PINK)
        c2 = Dot(plane.n2p(2-1.j), color=PINK)
        c3 = Dot(plane.n2p(-0.4-0.3j), color=PINK)
        G1 = Circle(radius=r1.get_value()).move_to(c1)
        G1.add_updater(lambda x: x.become(Circle(radius=r1.get_value()).move_to(c1)))
        G1_label = Tex("Disk 1").next_to(G1, UP, 0.03).scale(0.8)
        G2 = Circle(radius=r1.get_value()).move_to(c2)
        G2.add_updater(lambda x: x.become(Circle(radius=r1.get_value()).move_to(c2)))
        G2_label = Tex("Disk 2").next_to(G2, DOWN, 0.03).scale(0.8)
        G3 = Circle(radius=r3.get_value()).move_to(c3)
        G3.add_updater(lambda x: x.become(Circle(radius=r3.get_value()).move_to(c3)))
        G3_label = Tex("Disk 3").next_to(G3, UL, 0.03).scale(0.8)

        A_tex = MathTex("A").next_to(A, UP * 2)

        same_evalue_tex = MathTex(r"\sigma(A) = \sigma(D^{-1} A D)").next_to(A_tex, UP *2)
        self.play(Write(same_evalue_tex))
        self.wait(3)
