from manim import *


class Proof2(Scene):
    def construct(self):
        #圈出第k行
        title = Tex("Proof of Thm").shift(UP * 3.5)
        Formula_3 = MathTex(r"\begin{bmatrix} a_{11} & ... & a_{1n}\\ ... &  & ... \\a_{k1} & ... & a_{kn} \\... &  & ...\\ a_{n1} & ... & a_{nn} \end{bmatrix} "
                            r"\begin{bmatrix} x_1\\ ...\\ x_k \\ ... \\ x_n \end{bmatrix} = \lambda "
                            r"\begin{bmatrix} x_1\\ ...\\ x_k \\ ... \\ x_n \end{bmatrix}").shift(UP * 1.5)
        Formula_4 = MathTex(r"\lambda x_k", r"=", r"\sum_j", r"a_{kj}x_j")
        Formula_5 = MathTex(r"\lambda x_k", r"=", r"\sum_{j\ne k}", r"a_{kj}x_j", r"+", r"a_{kk}x_k")
        Formula_6 = MathTex(r"\lambda x_k", r" -a_{kk}x_k", r"=", r"\sum_{j"
                                                                  r"x\ne k}", r"a_{kj}x_j")
        Formula_7 = MathTex(r"(", r"\lambda", r"-a_{kk}", r")", r"x_k", r"=", r"\sum_{j\ne k}", r"a_{kj}x_j")
        Formula_Hint_1 = MathTex(r"\triangle \ne: |a+b|\le|a|+|b|").next_to(Formula_7, DOWN)
        Formula_8 = MathTex(r"|\lambda-a_{kk}||x_k|", r"=", r"|\sum_{j\ne k}", r"a_{kj}", r"x_j", r"|")
        Formula_9 = MathTex(r"|\lambda-a_{kk}||x_k|", r"\le", r"\sum_{j\ne k}", r"|a_{kj}|", r"|", r"x_j", r"|")
        Formula_10 = MathTex(r"|\lambda-a_{kk}||x_k|", r"\le", r"|a_{k1}|", r"|x_1|", r"+ ... +", r"|a_{k,k-1}|", r"|x_{k-1}|",
                             r"+", r"|a_{k,k+1}|", r"|x_{k+1}|", r"+ ... +", r"|a_{k,n}|", r"|x_n| ").scale(0.8)
        Formula_11 = MathTex(r"|\lambda-a_{kk}||x_k|", r"\le", r"|a_{k1}|", r"|x_k|", r"+ ... +", r"|a_{k,k-1}|",
                             r"|x_k}|", r"+", r"|a_{k,k+1}|", r"|x_k|", r"+ ... +", r"|a_{k,n}|", r"|x_k| ").scale(0.8)
        Formula_Hint_2 = MathTex(r"x \ is \ eigenvector, \ so \ |x_k|\ne 0").next_to(Formula_11, DOWN).scale(0.8)
        Formula_12 = MathTex(r"|\lambda-a_{kk}||x_k|", r"\le", r"(\sum_{j\ne k} |a_{kj}|)", r"|x_k|")
        Formula_13 = MathTex(r"|\lambda-a_{kk}|", r"\le", r"\sum_{j\ne k} |a_{kj}|")

        self.add(title)
        self.play(Write(Formula_3))
        self.wait()

        self.play(Write(Formula_4.next_to(Formula_3, DOWN)))
        self.wait()
        self.play(Unwrite(Formula_3))
        self.wait()
        self.play(Formula_4.animate.shift(UP))
        self.wait()

        self.play(TransformMatchingTex(Formula_4, Formula_5))
        self.wait()

        self.play(TransformMatchingTex(Formula_5, Formula_6))
        self.wait()

        self.play(TransformMatchingTex(Formula_6, Formula_7))
        self.wait()

        self.play(TransformMatchingTex(Formula_7, Formula_8))
        self.wait()

        self.play(Write(Formula_Hint_1))
        self.wait()
        self.remove(Formula_Hint_1)
        self.wait()

        self.play(TransformMatchingTex(Formula_8, Formula_9))
        self.wait()

        self.play(TransformMatchingTex(Formula_9, Formula_10))
        self.wait()

        self.play(TransformMatchingTex(Formula_10, Formula_11))
        self.wait()

        self.play(TransformMatchingTex(Formula_11, Formula_12))
        self.wait()

        self.play(Write(Formula_Hint_2))
        self.wait()
        self.remove(Formula_Hint_2)
        self.wait()

        self.play(TransformMatchingTex(Formula_12, Formula_13))
        self.wait()
#manim -pql Proof2.py Proof2
