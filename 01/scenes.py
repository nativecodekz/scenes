from manimlib import *
from manimlib.constants import DEFAULT_MOBJECT_TO_MOBJECT_BUFFER, ORIGIN, RIGHT, np
from manimlib.mobject.mobject import Mobject
from manimlib.mobject.types.vectorized_mobject import VMobject
import numpy as np
from math import sin, cos

class TrigonometrySubjectScene(Scene):
    def construct(self):
        self.play(Write(Text('Суть Тригонометрии')))
        self.wait()

class CosineAndSineScene(Scene):
    def construct(self):
        cosine = FunctionGraph(lambda x: cos(x), color=RED)
        self.play(ShowCreation(cosine))
        self.wait(1)
        sine = FunctionGraph(lambda x: sin(x), color=BLUE)
        self.play(ShowCreation(sine))
        self.wait()
        self.play(cosine.animate.shift(RIGHT * np.pi / 2))
        self.wait()

class CosineAndSineRotateScene(Scene):
    def construct(self):
        cosine = FunctionGraph(lambda x: cos(x), color=RED, x_range=[0, 30])
        self.play(ShowCreation(cosine))
        self.wait(1)
        sine = FunctionGraph(lambda x: sin(x), color=BLUE, x_range=[0, 30])
        self.play(ShowCreation(sine))
        self.wait()
        self.play(cosine.animate.rotate(-np.pi/2.0, about_point=cosine.get_center() + 15*LEFT + UP))
        self.play(cosine.animate.shift(2*DOWN + RIGHT), sine.animate.shift(RIGHT))
        cosTex = Tex('\\cos x', color=RED)
        sinTex = Tex('\\sin x', color=BLUE)
        cosTex.to_corner(UP + RIGHT)
        sinTex.next_to(cosTex.get_edge_center(DOWN), DOWN)
        self.play(ShowCreation(cosTex), ShowCreation(sinTex))

        # two lines
        x_line = Line(LEFT + DOWN, RIGHT + DOWN)
        y_line = Line(RIGHT + DOWN, RIGHT + UP)
        self.play(ShowCreation(x_line), ShowCreation(y_line))


        dot_x = Dot(DR, color=YELLOW)
        dot_y = Dot(RIGHT, color=YELLOW)
        dot_g = Dot(RIGHT, color=GREEN)

        dot_x.add_updater(lambda dot: dot.move_to( RIGHT * cos(cosine.get_coord(1) + 2.0) + DOWN ))
        dot_y.add_updater(lambda dot: dot.move_to( UP * -sin(sine.get_edge_center(LEFT)[0] - 1.0) + RIGHT ))

        line_x = Line(color=GREY_A)
        line_y = Line(color=GREY_A)

        self.play(ShowCreation(dot_y), ShowCreation(dot_x))
        self.wait(3)
        self.play(cosine.animate.shift(UP*20), sine.animate.shift(LEFT*20), run_time=20)
        self.wait()
        dot_g.add_updater(lambda dot: dot.move_to(np.array((dot_x.get_coord(0), dot_y.get_coord(1), .0,))))
        line_x.add_updater(lambda line: line.put_start_and_end_on(dot_x.get_center(), dot_g.get_center()))
        line_y.add_updater(lambda line: line.put_start_and_end_on(dot_y.get_center(), dot_g.get_center()))

        self.play(cosine.animate.shift(DOWN*20), sine.animate.shift(RIGHT*20), run_time=0)
        self.play(ShowCreation(line_x), ShowCreation(line_y), ShowCreation(dot_g))
        self.wait()
        self.play(cosine.animate.shift(UP*20), sine.animate.shift(LEFT*20), run_time=20)
        self.wait(3)
        self.play(cosine.animate.shift(DOWN*20), sine.animate.shift(RIGHT*20), run_time=0)
        self.remove(dot_g)
        
        circle = Circle(radius=1.0, color=GREY_A)
        self.play(FadeIn(circle), FadeIn(dot_g))
        self.play(cosine.animate.shift(UP*20), sine.animate.shift(LEFT*20), run_time=20)
        self.wait()
        self.play(cosine.animate.set_opacity(0.0), sine.animate.set_opacity(0.0))
        self.play(cosine.animate.shift(DOWN*20), sine.animate.shift(RIGHT*20), run_time=10)
        self.wait()
        



