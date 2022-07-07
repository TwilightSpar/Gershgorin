from manim import *
from numpy import linalg as LA
import numpy as np


class GDisk(Scene):
    def construct(self):
        a = Tex("$x=y$")
        self.play(Write(a))


#manim -pql Test.py GDisk
