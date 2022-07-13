from manim import *


class GDisk(Scene):
    def construct(self):
        Prop = Tex(r"Gershgorin $\leftrightarrow$ invertibility?")
        self.play(Write(Prop))
        self.wait(5)
        self.remove(Prop)

        matrix_content = [[1.5 + 1.5j, 1j],
                          [1.0, 1.1-0.7j]]
        matrix_object = Matrix(matrix_content,
                               h_buff=2,
                               left_bracket="(",
                               right_bracket=")",
                               element_alignment_corner=DOWN)

        plane = ComplexPlane(
            x_range=[-1, 3],
            y_range=[-2, 2.5]
        ).add_coordinates()

        r1 = ValueTracker(1.0)
        r2 = ValueTracker(1.0)
        c1 = Dot(plane.n2p(1.5 + 1.5j), color=YELLOW)
        c2 = Dot(plane.n2p(1.1-0.7j), color=YELLOW)
        G1 = Circle(radius=r1.get_value()).move_to(c1)
        G1.add_updater(lambda x: x.become(Circle(radius=r1.get_value()).move_to(c1)))
        G2 = Circle(radius=r2.get_value()).move_to(c2)
        G2.add_updater(lambda x: x.become(Circle(radius=r2.get_value()).move_to(c2)))

        group1 = Group(plane, c1, c2, G1, G2)
        group2 = Group(matrix_object, group1).arrange_in_grid(cols=2)
        self.add(group2)
        self.wait(2)
        origin = Dot(plane.get_origin(), color=YELLOW)
        origin_label = MathTex((0, 0)).next_to(origin, UP, 0.03).scale(0.5)
        self.play(Create(origin))
        self.play(Create(origin_label))
        self.wait(2)
        self.remove(origin_label)
        self.wait(2)
        self.play(r1.animate.set_value(2.3), run_time=0.6)
        self.play(r1.animate.set_value(1), run_time=0.6)
        self.play(r2.animate.set_value(1.5), run_time=0.6)
        self.play(r2.animate.set_value(1), run_time=0.6)
        self.wait(2)
        tex = Tex("Strictly Diagonally Dominant Matrix").next_to(group2, UP)
        self.play(Write(tex))
        self.wait(1)
        tex2 = MathTex(r"\sum_{i\ne k} |a_{ki}| < |a_{kk}|;\forall k").next_to(group2, DOWN)
        self.play(Write(tex2))
        self.wait(1)
