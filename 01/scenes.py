from manimlib import *
from manimlib.constants import DEFAULT_MOBJECT_TO_MOBJECT_BUFFER, ORIGIN, RIGHT, np
from manimlib.mobject.mobject import Mobject
from manimlib.mobject.types.vectorized_mobject import VMobject
import numpy as np
from math import sin, cos, atan2

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


class CosineAndSineGraphScene(Scene):
    def construct(self):
        x_axis = Line(LEFT_SIDE, RIGHT_SIDE, stroke_width=0.5)
        self.play(ShowCreation(x_axis))

        y_axis = Line(TOP, BOTTOM, stroke_width=0.5)
        self.play(ShowCreation(y_axis))

        circle = Circle(radius=1, color=GREY_A)
        self.play(ShowCreation(circle))
        self.wait()

        line = Line()
        dot_g = Dot(RIGHT, color=GREEN)
        line.add_updater(lambda l: l.put_start_and_end_on(ORIGIN, dot_g.get_center()))
        self.play(ShowCreation(line), ShowCreation(dot_g))
        self.wait()

        def dot_y_shifter(dot, dt):
            dot.set_y(dot_g.get_y())
            dot.shift(RIGHT * dt * 0.35)

        def dot_x_shifter(dot, dt):
            dot.set_x(dot_g.get_x())
            dot.shift(DOWN * dt * 0.35)

        # sine
        y_dot = Dot(LEFT_SIDE, color=YELLOW)
        y_line = Line(color=YELLOW, stroke_width=0.5)
        y_line.add_updater(lambda l: l.put_start_and_end_on(dot_g.get_center(), y_dot.get_center()))
        y_path = TracedPath(y_dot.get_center, stroke_color=BLUE)
        self.add(y_path)

        


        # cosine
        x_dot = Dot(TOP + RIGHT, color=YELLOW)
        x_line = Line(color=YELLOW, stroke_width=0.5)
        x_line.add_updater(lambda l: l.put_start_and_end_on(dot_g.get_center(), x_dot.get_center()))
        x_path = TracedPath(x_dot.get_center, stroke_color=RED)
        self.add(x_path)


        self.play(ShowCreation(y_dot), ShowCreation(y_line), ShowCreation(x_dot), ShowCreation(x_line))

        # labels
        cosTex = Tex('\\cos x', color=RED)
        sinTex = Tex('\\sin x', color=BLUE)
        cosTex.to_corner(UP + RIGHT)
        sinTex.next_to(cosTex.get_edge_center(DOWN), DOWN)
        self.play(ShowCreation(cosTex), ShowCreation(sinTex))


        # animate rotation
        y_dot.add_updater(dot_y_shifter)
        x_dot.add_updater(dot_x_shifter)
        self.play(MoveAlongPath(dot_g, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot_g, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot_g, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot_g, circle), run_time=4, rate_func=linear)
        self.play(MoveAlongPath(dot_g, circle), run_time=4, rate_func=linear)
        y_dot.remove_updater(dot_y_shifter)
        x_dot.remove_updater(dot_x_shifter)
        self.wait()

class CosineAndSineShift(Scene):
    def construct(self):
        # labels
        cosTex = Tex('\\cos x', color=RED)
        sinTex = Tex('\\sin x', color=BLUE)
        cosTex.to_corner(UP + RIGHT)
        sinTex.next_to(cosTex.get_edge_center(DOWN), DOWN)
        self.play(ShowCreation(cosTex), ShowCreation(sinTex))
        
        cosine = FunctionGraph(lambda x: cos(x), color=RED,x_range=[-20, 20])
        cosine.shift(RIGHT * np.pi / 2)
        self.play(ShowCreation(cosine))
        self.wait(1)
        sine = FunctionGraph(lambda x: sin(x), color=BLUE,x_range=[-20, 20])
        self.play(ShowCreation(sine))
        self.wait(3)
        self.play(cosine.animate.shift(LEFT * np.pi / 2))
        
        dot1 = Dot(UP, color=YELLOW)
        dot2 = Dot(UP + RIGHT * np.pi/2, color=YELLOW)
        self.play(ShowCreation(dot1), ShowCreation(dot2))

        vg = VGroup(dot1, dot2)

        brace = Brace(vg, UP)
        self.play(ShowCreation(brace))

        tex1 = Tex('{ \\pi \\over { 2 } } rad')
        tex1.next_to(brace.get_center(), UP)
        self.play(ShowCreation(tex1))
        self.wait()

class CosineAndSineAxisAngle(Scene):
    def construct(self):
        x_axis = Line(LEFT_SIDE, RIGHT_SIDE)
        self.play(ShowCreation(x_axis))

        y_axis = Line(TOP, BOTTOM)
        self.play(ShowCreation(y_axis))


        x_label = Tex('x')
        x_label.next_to(RIGHT_SIDE / 2, DOWN)

        y_label = Tex('y')
        y_label.next_to(TOP / 2, LEFT)

        self.play(ShowCreation(x_label), ShowCreation(y_label))

        angle = Arc(np.pi/2, -np.pi/2)
        self.play(ShowCreation(angle))
        self.wait()

        degree = Tex('90 \\circ')
        degree.move_to(angle.get_corner(UR))

        self.play(Write(degree))
        self.wait()

class AboutRadiansScene(Scene):
    def construct(self):
        tex1 = Tex('180 \\circ = \\pi rad')
        self.play(Write(tex1))
        self.wait(5)
        self.play(tex1.animate.to_edge(UP))
        self.wait()

        # angle
        line1 = Line(ORIGIN, RIGHT * 3)
        line2 = Line(ORIGIN, RIGHT * 3)

        self.play(ShowCreation(line1), ShowCreation(line2))
        self.wait()
        self.play(line2.animate.rotate_about_origin(np.pi/3))
        self.wait()
        angle = Arc(0, np.pi/3)
        self.play(ShowCreation(angle))
        self.wait()
        arc = Arc(0, np.pi/3, radius=3.0, color=RED)
        self.play(TransformFromCopy(angle, arc))
        self.wait()
        txt1 = Text('угол * радиус')
        txt1.next_to(arc, RIGHT)
        self.play(ShowCreation(txt1))
        self.wait(3)
        self.play(Uncreate(Group(line1, line2, angle, arc, txt1, tex1)))
        self.wait()
        tex2 = Tex('rad =  \\frac { \\pi deg }{ 180 }')
        txt2 = Text('deg - градусы', font_size=20)
        txt2.next_to(tex2, DOWN)
        self.play(Write(tex2), Write(txt2))
        self.wait()
        tex3 = Tex('deg = \\frac { 180rad } { \\pi }')
        self.play(ReplacementTransform(tex2, tex3))
        self.wait()

class LengthDefinition(Scene):
    def construct(self):
        coords = NumberPlane(opacity=0.5)
        self.play(ShowCreation(coords))
        self.wait()

        # draw point
        dot = Dot(RIGHT * 4 + UP * 3, color=YELLOW)
        line = Line(ORIGIN, dot.get_center(),color=RED)
        self.play(ShowCreation(line), FadeIn(dot))
        self.wait()
        self.play(Flash(line))
        self.wait(3)

        line2 = Line(ORIGIN, UP * 3,color=RED)
        self.play(ShowCreation(line2))
        self.wait()
        self.play(line2.animate.shift(RIGHT * 4))
        self.wait()
        line3 = Line(ORIGIN, RIGHT * 4, color=RED)
        self.play(ShowCreation(line3))
        self.wait()

        label_x = Tex('x')
        label_y = Tex('y')
        label_c = Tex('c')

        label_x.next_to(line3, DOWN)
        label_y.next_to(line2, RIGHT)
        label_c.next_to(line, UL).shift(-1.5*UL)

        self.play(FadeIn(label_x), FadeIn(label_y), FadeIn(label_c))
        self.wait()

        # show formulae
        formulae = Tex(*'c^2 = x^2+y^2', color=YELLOW)
        formulae.shift(DOWN)
        self.play(Write(formulae[0:3]))
        self.wait()
        self.play(TransformFromCopy(label_x, formulae[3:5]))
        self.wait()
        self.play(Write(formulae[5]))
        self.wait()
        self.play(TransformFromCopy(label_y, formulae[6:]))
        self.wait()
        self.play(Uncreate(coords))
        self.wait()
        self.play(Uncreate(Group(dot, line, line2, line3, label_x, label_y, label_c)))
        self.play(formulae.animate.center())
        self.wait()

class CosineAndSineDefinition(Scene):
    def construct(self):
        # triangle
        a = Line(ORIGIN, RIGHT*4)
        b = Line(RIGHT*4, RIGHT*4 + UP*3)
        c = Line(ORIGIN, RIGHT*4 + UP*3)

        arc = Arc(0, atan2(3, 4))

        label_a = Tex('a').next_to(a, DOWN)
        label_b = Tex('b').next_to(b, RIGHT)
        label_c = Tex('c').next_to(c, UL).shift(-UL*1.5)
        label_alpha = Tex('\\alpha').next_to(arc, RIGHT)

        tr = VGroup(a, b, c, label_a, label_b, label_c, arc, label_alpha).center()
        self.play(ShowCreation(tr))
        self.play(tr.animate.to_edge(LEFT))

        # cos
        cosine = Tex('\\cos \\alpha = \\frac { a } { c } ')
        self.play(Write(cosine))
        self.play(cosine.animate.shift(UP))

        sine = Tex('\\sin \\alpha = \\frac { b } { c } ').next_to(cosine, DOWN)
        self.play(Write(sine))
        self.wait()
