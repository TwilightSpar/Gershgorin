from manim import *


class GDisk(Scene):
    def construct(self):
        # Prop = Tex(r"Gershgorin $\leftrightarrow$ invertibility?")
        # self.play(Write(Prop))
        # self.wait(5)
        # self.remove(Prop)

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

        group1 = Group(plane, c1, c2, c3, G1, G2, G3, G1_label, G2_label, G3_label)

        self.add(group1)
        self.add(A)

        A_tex = MathTex("A").next_to(A, UP * 2)
        self.play(Create(A_tex))
        self.wait(2)
        origin = Dot(plane.get_origin(), color=YELLOW)
        origin_label = MathTex((0, 0)).next_to(origin, UP, 0.03).scale(0.8)
        self.play(Create(origin))
        self.play(Create(origin_label))
        self.wait(2)
        self.remove(origin_label)
        self.wait(2)

        D = MathTex(r"\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1+\epsilon \end{pmatrix}").scale(0.6).next_to(A, RIGHT)
        D_inv = MathTex(r"\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \frac{1}{1+\epsilon} \end{pmatrix}").scale(0.6).next_to(A, LEFT)

        D_inv_tex = MathTex("D^{-1}").next_to(D_inv, UP*2)
        D_inv_tex.generate_target()
        D_inv_tex.target.next_to(A_tex, LEFT)

        D_tex = MathTex("D").next_to(D, UP * 2)
        D_tex.generate_target()
        D_tex.target.next_to(A_tex, RIGHT)

        self.play(Create(D_inv))
        self.play(Create(D_inv_tex))
        self.play(Create(D))
        self.play(Create(D_tex))
        self.wait(2)

        self.play(MoveToTarget(D_inv_tex))

        D_inv_A = MathTex(r"\begin{pmatrix} 1+j & 0.2 & 0.2 \\ 0.2 & 2-j & 0.2 \\ \frac{1}{1+\epsilon} 0.2 & \frac{1}{1+\epsilon} 0.3 & \frac{1}{1+\epsilon}(-0.4-0.3j) \end{pmatrix}").scale(0.6).shift(3 * LEFT)
        self.remove(D_inv)
        self.play(ReplacementTransform(A, D_inv_A), run_time=2)

        self.play(MoveToTarget(D_tex))

        D_inv_A_D = MathTex(
            r"\begin{pmatrix} 1+j & 0.2 & (1+\epsilon)0.2 \\ 0.2 & 2-j & (1+\epsilon)0.2 \\ \frac{1}{1+\epsilon} 0.2 & \frac{1}{1+\epsilon} 0.3 & -0.4-0.3j \end{pmatrix}").scale(
            0.6).shift(2.5 * LEFT)
        self.remove(D)
        self.play(ReplacementTransform(D_inv_A, D_inv_A_D), run_time=2)
        self.play(D_inv_A_D.animate.scale(1.4))

        self.wait(3)
        self.play(r1.animate.set_value(1), run_time=2)
        self.play(r3.animate.set_value(0.3), run_time=2)
        self.wait(2)
