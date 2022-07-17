from manim import *


class Thanks(Scene):
    def construct(self):
        Special_Thanks = Text("Special Thanks to:", font_size=60, color=BLUE).align_on_border(UP)
        self.play(Write(Special_Thanks))

        font_size = 35
        # Fish = Text(
        #     "Professor Donniell Fishkind (Johns Hopkins U of AMS Department) with the help of proof idea",font_size=font_size).next_to(Special_Thanks,DOWN)
        # WG = Text("Geng Wang with the help of the animation making",font_size=font_size)
        # ZSQ = Text("Bill Zhang with the help of video audit",font_size=font_size)

        Fish = "Professor Donniell Fishkind (Johns Hopkins U of AMS Department) with the help of proof idea"
        WG = "Geng Wang with the help of the animation making"
        ZSQ = "Bill Zhang with the help of video audit"
        blist = BulletedList(Fish, WG, ZSQ, font_size=font_size, buff=1.2).next_to(Special_Thanks, DOWN*2)
        self.play(Create(blist))
        self.wait(2)
