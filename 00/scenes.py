from manimlib import *
from manimlib.constants import DEFAULT_MOBJECT_TO_MOBJECT_BUFFER, ORIGIN, RIGHT, np
from manimlib.mobject.mobject import Mobject
from manimlib.mobject.types.vectorized_mobject import VMobject
import numpy as np

class Scene0(Scene):
    def indicate_rect(self, rect : Rectangle):
        rect.save_state()
        return Succession(rect.animate.set_fill(YELLOW, opacity=0.6), Restore(rect), run_time=1)


    def construct(self):
        f1 = Tex("(", "a", "+", "b", ")", "\\times ", "c", "=", "a", "c",  "+", "b", "c")
        txt1 = Text("Распределительный закон умножения")
        group = VGroup(f1, txt1).arrange(DOWN, buff=1)
        self.play(Write(f1))
        self.wait(3)
        self.play(Write(txt1))
        self.wait(5)
        self.play(Indicate(f1[6]))
        self.wait()
        self.play(Indicate(f1[0:5]))
        self.wait(3)
        self.play(Indicate(VGroup(f1[9], f1[12])))
        self.wait()
        self.play(Indicate(VGroup(f1[8], f1[11])))
        self.wait()
        self.play(Indicate(f1[10]))
        self.wait()
        self.play(Indicate(VGroup(f1[8], f1[9], f1[11], f1[12])))
        self.wait(5)
        self.play(FadeOut(txt1))
        group.remove(f1)
        f1.generate_target()
        f1.target.to_edge(UP)
        self.play(MoveToTarget(f1))
        self.wait()

        rect1 = Rectangle(2.0, 3.0)
        rect2 = Rectangle(3.0, 3.0)

        rect1.center()
        rect2.next_to(rect1, buff=0.0)
        
        vg = VGroup(rect1, rect2)

        # labels
        texA = Tex("a")
        texP = Tex("+")
        texB = Tex("b")
        texA.next_to(rect1.get_edge_center(UP), UP)
        texB.next_to(rect2.get_edge_center(UP), UP)
        texP.next_to(vg.get_edge_center(UP), UP)
        texP.shift(0.5*LEFT)
        vg += texA
        vg += texP
        vg += texB

        texC1 = Tex("c")
        texC2 = Tex("c")
        texC1.next_to(rect1.get_edge_center(LEFT), LEFT)
        texC2.next_to(rect2.get_edge_center(RIGHT), RIGHT)
        vg += texC1
        vg += texC2

        # ac
        texAC = Tex("ac")
        texAC.move_to(rect1)
        vg += texAC

        
        # bc
        texBC = Tex("bc")
        texBC.move_to(rect2)
        vg += texBC

        vg.center()

        self.play(Write(vg))
        self.wait()

        # a + b x c
        self.play(Indicate(VGroup(texA, texP, texB)))
        self.wait()
        self.play(Indicate(VGroup(texC1, texC2)))
        self.wait()


        # indicate ac
        self.play(self.indicate_rect(rect1), Indicate(VGroup(f1[8], f1[9])), run_time=3)
        self.wait(3)
        self.play(self.indicate_rect(rect2), Indicate(VGroup(f1[11], f1[12])), run_time=3)
        self.wait(3)
        self.play(self.indicate_rect(rect1), self.indicate_rect(rect2), Indicate(f1[10]), run_time=3)
        self.wait()


class LabelledRectangle(Rectangle):
    def __init__(self, width: float | None = None, height: float | None = None, **kwargs):
        super().__init__(width, height, **kwargs)

        # Add labels
        if 'wposition' not in kwargs:
            kwargs['wposition'] = TOP

        if 'hposition' not in kwargs:
            kwargs['hposition'] = LEFT

        self.wposition = kwargs['wposition']
        self.hposition = kwargs['hposition']

        if 'wlabel' in kwargs:
            self.wlabel = kwargs['wlabel']
            self.wlabel.next_to(self.get_edge_center(self.wposition), self.wposition)

        if 'hlabel' in kwargs:
            self.hlabel = kwargs['hlabel']
            self.hlabel.next_to(self.get_edge_center(self.hposition), self.hposition)

        if 'clabel' in kwargs:
            self.clabel = kwargs['clabel']
            self.clabel.move_to(self.get_center())

    def update_labels(self):
        if self.wlabel:
            self.wlabel.next_to(self.get_edge_center(self.wposition), 0.3*self.wposition)

        if self.hlabel:
            self.hlabel.next_to(self.get_edge_center(self.hposition), self.hposition)

        if self.clabel:
            self.clabel.move_to(self.get_center())


class RectanglesGroup(VGroup):
    def __init__(self):
        super().__init__()

        a = 4.0
        b = 3.0
        c = 2.0
        d = 1.0

        # Add rectangles
        self.ac = ac = LabelledRectangle(a, c, wlabel=Tex('a'), hlabel=Tex('c'), clabel=Tex('ac'))
        self.ad = ad = LabelledRectangle(a, d, wlabel=Tex('a'), hlabel=Tex('d'), clabel=Tex('ad'), wposition=BOTTOM)
        self.bc = bc = LabelledRectangle(b, c, wlabel=Tex('b'), hlabel=Tex('c'), clabel=Tex('bc'), hposition=RIGHT)
        self.bd = bd = LabelledRectangle(b, d, wlabel=Tex('b'), hlabel=Tex('d'), clabel=Tex('bd'), wposition=BOTTOM, hposition=RIGHT)
        self.apb1 = Tex('+')
        self.apb2 = Tex('+')
        self.cpd1 = Tex('+')
        self.cpd2 = Tex('+')

        # add
        self.add(ac)
        self.add(ad)
        self.add(bc)
        self.add(bd)

        # positions
        ad.next_to(ac.get_edge_center(BOTTOM), BOTTOM, buff=0)
        bc.next_to(ac.get_edge_center(RIGHT), RIGHT, buff=0)
        bd.next_to(bc.get_edge_center(BOTTOM), BOTTOM, buff=0)


        self.center()

        ac.update_labels()
        ad.update_labels()
        bc.update_labels()
        bd.update_labels()
        
        self.apb1.next_to(self.get_edge_center(UP), UP)
        self.apb2.next_to(self.get_edge_center(BOTTOM), 0.3*BOTTOM)
        self.cpd1.next_to(self.get_edge_center(LEFT), LEFT + 0.1*BOTTOM)
        self.cpd2.next_to(self.get_edge_center(RIGHT), RIGHT + 0.1*BOTTOM)



class BracketByBracketScene(Scene):
    def construct(self):
        f = Tex(*'(a+b)(c+d)=ac+ad+bc+bd')
        self.play(Write(f[0:11]))
        self.wait()
        self.play(TransformFromCopy(f[1], f[11], path_arc=np.pi)) # a -> a
        self.play(TransformFromCopy(f[6], f[12], path_arc=np.pi)) # c -> c
        self.play(Write(f[13]))
        self.play(TransformFromCopy(f[1], f[14], path_arc=np.pi)) # a -> a
        self.play(TransformFromCopy(f[8], f[15], path_arc=np.pi)) # d -> d
        self.play(Write(f[16]))
        self.play(TransformFromCopy(f[3], f[17], path_arc=np.pi)) # b -> b
        self.play(TransformFromCopy(f[6], f[18], path_arc=np.pi)) # c -> c
        self.play(Write(f[19]))
        self.play(TransformFromCopy(f[3], f[20], path_arc=np.pi)) # b -> b
        self.play(TransformFromCopy(f[8], f[21], path_arc=np.pi)) # d -> d
        self.wait()
        self.play(f.animate.to_edge(UP))
        self.wait()
        
        # Rectangle animations
        rg = RectanglesGroup()
        self.play(FadeInFromPoint(rg, ORIGIN))
        self.wait()

        # sides
        self.play(TransformFromCopy(f[1:4], Group(rg.ac.wlabel, rg.apb1, rg.bc.wlabel)))
        self.play(TransformFromCopy(f[1:4], Group(rg.ad.wlabel, rg.apb2, rg.bd.wlabel)))
        self.play(TransformFromCopy(f[6:9], Group(rg.ac.hlabel, rg.cpd1, rg.ad.hlabel)))
        self.play(TransformFromCopy(f[6:9], Group(rg.bc.hlabel, rg.cpd2, rg.bd.hlabel)))

        # names of rectangles
        self.play(TransformFromCopy(f[11:13], rg.ac.clabel))
        self.play(TransformFromCopy(f[14:16], rg.ad.clabel))
        self.play(TransformFromCopy(f[17:19], rg.bc.clabel))
        self.play(TransformFromCopy(f[20:22], rg.bd.clabel))
        self.wait()


class SquareOfSum(Scene):
    def construct(self):
        f = Tex(*'(a+b)^2=(a+b)(a+b)=aa+ab+ba+bb')
        self.play(Write(f[0:7]))
        self.wait()
        self.play(Write(f[7:18]))
        self.wait()

        # formula animation

        # aa
        self.play(TransformFromCopy(f[8], f[18]), path_arc=np.pi)
        self.play(TransformFromCopy(f[13], f[19]), path_arc=np.pi)
        self.play(Write(f[20]))

        # ab
        self.play(TransformFromCopy(f[8], f[21]), path_arc=np.pi)
        self.play(TransformFromCopy(f[15], f[22]), path_arc=np.pi)
        self.play(Write(f[23]))

        # ba
        self.play(TransformFromCopy(f[10], f[24]), path_arc=np.pi)
        self.play(TransformFromCopy(f[13], f[25]), path_arc=np.pi)
        self.play(Write(f[26]))

        # bb
        self.play(TransformFromCopy(f[10], f[27]), path_arc=np.pi)
        self.play(TransformFromCopy(f[15], f[28]), path_arc=np.pi)
        self.wait()

        # replace aa -> a2
        f1 = Tex('a^2')
        f1.move_to(f[18:20].get_center()).shift(0.1*UP)
        self.play(Transform(f[18:20], f1))

        # replace ba -> ab
        f2 = Tex('ab')
        f2.move_to(f[24:26].get_center())
        self.play(Transform(f[24:26], f2))

        # replace bb -> b^2
        f3 = Tex('b^2')
        f3.move_to(f[27:29].get_center())
        self.play(Transform(f[27:29], f3))

        # group ab -> 2ab
        f4 = Tex('a^2+2ab+b^2')
        f4.next_to(f[18].get_edge_center(RIGHT), buff=0).shift(0.4*LEFT)
        self.play(Transform(Group(f1, f2, f3, f[18:29]), f4))



class SquareOfDiff(Scene):
    def construct(self):
        f = Tex('(a-b)^2')
        f.save_state()
        self.play(Write(f))
        self.wait()
        f1 = Tex('(a+(-b))^2')
        self.play(ReplacementTransform(f, f1))
        self.wait()
        f2 = Tex('=a^2+a(-b)+a(-b)+b^2')
        f2.next_to(f1.get_edge_center(RIGHT), RIGHT, buff=0)
        self.play(Write(f2))
        self.play(Group(f1, f2).animate.center())
        self.wait(3)
        f3 = Tex('=a^2-ab-ab+b^2')
        f3.next_to(f1.get_edge_center(RIGHT), RIGHT, buff=0)
        self.play(ReplacementTransform(f2, f3))
        self.wait(3)
        f4 = Tex('=a^2-2ab+b^2')
        f4.next_to(f1.get_edge_center(RIGHT), RIGHT, buff=0)
        self.play(ReplacementTransform(f3, f4))
        self.play(Group(f1, f4).animate.center())
        self.wait()
        f.restore()
        f.shift(LEFT*1.5)
        self.play(Uncreate(f1), Write(f))
        self.wait()

class NativeCodeIntro(Scene):
    def construct(self):
        txt = Text('Native Code').scale(1.5)
        self.play(Write(txt))
        self.wait(2)
        self.play(Uncreate(txt))
        self.wait()

class GoldenRuleTitle(Scene):
    def construct(self):
        txt = Text('Золотое правило алгебры')
        self.play(Write(txt))
        self.wait(2)
        txt2 = Text('Делайте с одной частью уравнения то,', font_size=24)
        txt3 = Text('что вы делаете с другой!', font_size=24)

        tg = Group(txt2, txt3)
        tg.arrange(DOWN)

        self.play(txt.animate.shift(UP), ShowCreation(tg))
        self.wait()

class GoldenRuleDemonstration(Scene):
    def construct(self):
        f = Tex(*'5+3=6+2+7')
        f1 = Tex(*'5+3+7=6+2+7')
        self.play(Write(f[0:7]))
        self.wait(3)
        self.play(Write(f[7:9]))
        self.play(Indicate(f[7:9]))
        self.wait(2)
        self.play(TransformMatchingTex(f, f1, path_arc=-np.pi/2))
        self.wait()
        self.play(Indicate(Group(f1[3:5], f1[9:11])))
        self.wait(3)
        self.play(Uncreate(f1))
        
        f = Tex(*'a+b=c-a')
        f1 = Tex(*'a+b=(c-a)^2')
        self.play(Write(f))
        self.wait()
        self.play(TransformMatchingTex(f, f1))
        self.wait()
        f2 = Tex(*'(a+b)^2=(c-a)^2')
        self.play(TransformMatchingTex(f1, f2))
        self.wait(3)
        self.play(Uncreate(f2))
        self.play(Write(f))
        self.wait()
        f3 = Tex(*'a^2+b=c-a^2')
        self.play(TransformMatchingTex(f, f3))
        self.wait()
        f4 = Tex('a', '^', '2', '+', 'b', '\\neq ', 'c', '-', 'a', '^', '2')
        self.play(TransformMatchingTex(f3, f4))
        self.wait()
        f5 = Tex(*'a+b=c-a')
        self.play(Uncreate(f4))
        self.play(Write(f5))
        self.wait()
        f6 = Tex(*'(a+b)d=(c-a)d')
        self.play(TransformMatchingTex(f5, f6))
        self.wait()
        f7 = Tex(*'ad+bd=cd-ad')
        self.play(TransformMatchingTex(f6, f7))
        self.wait()


class SquareEquation(Scene):
    def construct(self):
        f1 = Tex('x', '+', '10', '=', '{60', '\\over ', 'x}')
        self.play(Write(f1))
        self.wait(3)
        f2 = Tex('(', 'x' , '+', '10', ')', '^', '2', '=', '(', '\\frac{60' + '}{' + 'x}', ')', '^', '2')
        self.play(TransformMatchingTex(f1, f2))
        self.wait(2)
        self.play(TransformMatchingTex(f2, f1))
        self.wait(3)
        self.play(Indicate(VGroup(f1[2], f1[4])))
        self.wait()
        self.play(Indicate(VGroup(f1[0], f1[6])))
        f3 = Tex('(x', '+', '10)', 'x', '=', '{60', '\\over ', 'x}', 'x')
        self.play(TransformMatchingTex(f1, f3))
        self.wait()
        f4 = Tex('(x', '+', '10)', 'x', '=', '{60', 'x', '\\over ', 'x}')
        self.play(TransformMatchingTex(f3, f4))
        self.wait()
        self.play(Indicate(f4[6]))
        self.play(Indicate(f4[8]))
        self.wait()
        f5 = Tex('(x', '+', '10)', 'x', '=' '60')
        self.play(TransformMatchingTex(f4, f5, path_arc=-np.pi/2))
        self.wait(3)
        f6 = Tex('xx', '+', '10', 'x', '=', '60')
        self.play(TransformMatchingTex(f5, f6, path_arc=-np.pi/2))
        self.wait()
        f7 = Tex('x^2', '+', '10', 'x', '=', '60')
        self.play(TransformMatchingTex(f6, f7, path_arc=-np.pi/2))
        self.wait()
        self.play(f7.animate.to_edge(UP))

        # square
        xx = Rectangle(2.0, 2.0)
        self.play(ShowCreation(xx))
        x_label1 = Tex('x')
        x_label2 = Tex('x')
        x_label1.next_to(xx.get_edge_center(UP), UP)
        x_label2.next_to(xx.get_edge_center(LEFT), LEFT)
        self.play(AnimationGroup(TransformFromCopy(f7[0], x_label1), TransformFromCopy(f7[0], x_label2)))
        self.wait()

        x10 = Rectangle(5.0, 2.0)
        x_label3 = Tex('x')
        ten_label = Tex('10')
        x10.next_to(xx.get_edge_center(RIGHT), RIGHT, buff=0.0)
        self.play(ShowCreation(x10))
        self.play(VGroup(xx, x10, x_label1, x_label2).animate.center())
        self.wait()
        x_label3.next_to(x10.get_edge_center(RIGHT), RIGHT)
        ten_label.next_to(x10.get_edge_center(UP), UP)
        self.play(AnimationGroup(TransformFromCopy(f7[3], x_label3), TransformFromCopy(f7[2], ten_label)))
        self.wait(3)
        self.play(AnimationGroup(xx.animate.set_fill(YELLOW, opacity=0.7), x10.animate.set_fill(YELLOW, opacity=0.7), Indicate(f7[5])))
        self.play(xx.animate.set_fill(YELLOW, opacity=0.0), x10.animate.set_fill(YELLOW, opacity=0.0))
        self.wait()
        self.play(x10.animate.set_fill(YELLOW, opacity=0.7))
        self.play(x10.animate.set_fill(YELLOW, opacity=0.0))
        self.wait()

        x5_1 = Rectangle(2.5, 2.0)
        x5_2 = Rectangle(2.5, 2.0)

        x5_2.next_to(x5_1.get_edge_center(RIGHT), RIGHT, buff=0.0)
        VGroup(x5_1, x5_2).move_to(x10.get_center())

        self.play(FadeOut(VGroup(x10, ten_label)), FadeIn(VGroup(x5_1, x5_2)))
        self.wait()

        five_label1 = Tex('5')
        five_label2 = Tex('5')

        five_label1.next_to(x5_1.get_edge_center(UP), UP)
        five_label2.next_to(x5_2.get_edge_center(UP), UP)
        self.play(FadeIn(VGroup(five_label1, five_label2)))
        self.wait(3)
        self.play(FadeOut(VGroup(five_label2, x_label3)))
        self.play(x5_2.animate.rotate(np.pi/2.0))
        self.wait()
        self.play(x5_2.animate.next_to(xx.get_edge_center(BOTTOM), BOTTOM, buff=0.0).shift(0.25*DOWN))
        self.wait()
        five_label2.next_to(x5_2.get_edge_center(LEFT), LEFT).shift(0.25*RIGHT)
        x_label3.next_to(x5_2.get_edge_center(DOWN), DOWN).shift(0.25*DOWN)
        self.play(FadeIn(VGroup(five_label2, x_label3)))
        self.play(VGroup(xx, x5_1, x5_2, x_label1, x_label2, x_label3, five_label1, five_label2).animate.center().scale(0.8))
        self.wait()
        twenty_five_square = Rectangle(2.5, 2.5).scale(0.8)
        twenty_five_square.move_to(x5_1.get_edge_center(DOWN), UP)
        self.play(FadeIn(twenty_five_square))
        self.wait()
        self.play(xx.animate.set_fill(YELLOW, opacity=0.7), x5_1.animate.set_fill(YELLOW, opacity=0.7), x5_2.animate.set_fill(YELLOW, opacity=0.7), Indicate(f7[5]))
        self.play(xx.animate.set_fill(YELLOW, opacity=0.0), x5_1.animate.set_fill(YELLOW, opacity=0.0), x5_2.animate.set_fill(YELLOW, opacity=0.0))
        self.wait()
        self.play(twenty_five_square.animate.set_fill(YELLOW, opacity=0.7))
        self.play(twenty_five_square.animate.set_fill(YELLOW, opacity=0.0))

        # sides
        twenty_five_label = Tex('25')
        twenty_five_label.move_to(twenty_five_square.get_center())
        self.play(TransformFromCopy(VGroup(five_label1, five_label2), twenty_five_label))
        self.wait()

        # add 25
        f8 = Tex('x^2', '+', '10', 'x', '+', '25' '=', '60', '+', '25')
        f8.move_to(f7)
        self.play(TransformMatchingTex(f7, f8, path_arc=-np.pi/2))
        self.wait()
        f9 = Tex('x^2', '+', '10', 'x', '+', '25' '=', '85')
        f9.move_to(f8)
        self.play(TransformMatchingTex(f8, f9, path_arc=-np.pi/2))
        self.wait()
        self.play(xx.animate.set_fill(YELLOW, opacity=0.7), x5_1.animate.set_fill(YELLOW, opacity=0.7), x5_2.animate.set_fill(YELLOW, opacity=0.7), twenty_five_square.animate.set_fill(YELLOW, opacity=0.7), Indicate(f9[6]))
        self.play(xx.animate.set_fill(YELLOW, opacity=0.0), x5_1.animate.set_fill(YELLOW, opacity=0.0), x5_2.animate.set_fill(YELLOW, opacity=0.0), twenty_five_square.animate.set_fill(YELLOW, opacity=0.0))
        self.wait(3)
        vg = VGroup(xx, x5_1, x5_2, x_label1, x_label2, x_label3, five_label1, five_label2, twenty_five_square, twenty_five_label)
        self.play(vg.animate.to_edge(LEFT))
        self.wait()
        f10 = Tex('x', '+', '5', '=', '\\sqrt{ 85 }')
        self.play(TransformFromCopy(x_label1, f10[0]), Write(f10[1]), TransformFromCopy(five_label1, f10[2]), Write(f10[3]))
        self.play(TransformFromCopy(f9[6], f10[4]))
        self.wait()
        f11 = Tex('x', '=', '\\sqrt{ 85 }', '-', '5')
        self.play(TransformMatchingTex(f10, f11, path_arc=-np.pi/2))
        self.wait()

class SquareEquationTest(Scene):
    def construct(self):
        f1 = Tex('x', '+', '10', '=', '{60', '\\over ', 'x}')
        self.play(Write(f1))
        self.wait(3)
        f2 = Tex('(\\sqrt{ 85 } - 5)', '+', '10', '=', '{ 60 \\over ', '(\\sqrt{ 85 } - 5)', ' }')
        self.play(TransformMatchingTex(f1, f2, path_arc=-np.pi))
        self.wait(3)
        f3 = Tex('(\\sqrt{ 85 } - 5)', '^2', '+', '10', '(\\sqrt{ 85 } - 5)', '=', '60')
        self.play(TransformMatchingTex(f2, f3, path_arc=-np.pi))
        self.wait()
        self.play(Indicate(f3[0]))
        self.wait()
        f4 = Tex('85', '+', '25', '-', '10\\sqrt{ 85 }', '+', '10', '(\\sqrt{ 85 } - 5)', '=', '60')
        self.play(TransformMatchingTex(f3, f4))
        self.wait()
        f5 = Tex('110', '-', '10\\sqrt{ 85 }', '+', '10', '(\\sqrt{ 85 } - 5)', '=', '60')
        self.play(TransformMatchingTex(f4, f5))
        self.wait()
        self.play(Indicate(f5[5]))
        self.wait(3)
        f6 = Tex('110', '-', '10\\sqrt{ 85 }', '+', '10\\sqrt{ 85 } ', '-', '50', '=', '60')
        self.play(TransformMatchingTex(f5, f6))
        self.wait()
        self.play(Indicate(VGroup(f6[2], f6[4])))
        self.wait()
        self.play(Indicate(VGroup(f6[1], f6[3])))
        self.wait(3)
        f7 = Tex('110', '-', '50', '=', '60')
        self.play(TransformMatchingTex(f6, f7))
        self.wait()
        f8 = Tex('60', '=', '60')
        self.play(TransformMatchingTex(f7, f8))
        self.wait()

class SquareRootNote(Scene):
    def construct(self):
        f1 = Tex('5^2=(-5)^2=25')
        self.play(Write(f1))
        self.wait(3)
        self.play(f1.animate.shift(UP))
        f2 = Tex('\\sqrt{ 25 } = ')
        txt1 = Text('5 или -5?')
        txt2 = Text('5')
        txt1.next_to(f2.get_edge_center(RIGHT), RIGHT)
        txt2.next_to(f2.get_edge_center(RIGHT), RIGHT)
        VGroup(f2, txt1).center()
        self.play(Write(f2), Write(txt1))
        self.wait(3)
        self.play(Transform(txt1, txt2))
        self.wait(3)
        self.play(Uncreate(VGroup(txt1, txt2, f1, f2)))
        f3 = Tex(*'x=\\frac{-b\\pm\\sqrt{b^2-4ac}}{2a}')
        self.play(Write(f3))
        self.wait(3)
        self.play(Indicate(f3[4]))
        self.wait()

class PythagoreanTheoremTitle(Scene):
    def construct(self):
        self.play(Write(Text('Теорема Пифагора')))
        self.wait()

def indicatePolygon(p: Polygon):
    p.save_state()
    return Succession(p.animate.set_fill(YELLOW, opacity=0.6), Restore(p), run_time=1)

class PythagoreanTheoremForSquare(Scene):
    def construct(self):
        rect = Rectangle(3.0, 3.0)
        self.play(ShowCreation(rect))
        a_label1 = Tex('a')
        a_label2 = Tex('a')
        a_label1.next_to(rect.get_edge_center(UP), UP)
        a_label2.next_to(rect.get_edge_center(LEFT), LEFT)
        self.play(FadeIn(a_label1), FadeIn(a_label2))
        self.wait()
        diag = Line(rect.get_corner(DL), rect.get_corner(UR))
        self.play(ShowCreation(diag))
        c_label1 = Tex('c')
        c_label1.shift(UL*0.25)
        self.play(FadeIn(c_label1))
        self.play(Flash(diag), Indicate(c_label1))
        self.wait()

        # replace with two triangles
        tr1 = Polygon(rect.get_corner(UR), rect.get_corner(UL), rect.get_corner(DL))
        tr2 = Polygon(rect.get_corner(DR), rect.get_corner(UR), rect.get_corner(DL))
        self.play(FadeOut(rect), FadeOut(diag), FadeIn(tr1), FadeIn(tr2))
        self.wait()
        vg1 = VGroup(tr1, tr2)
        vg2 = vg1.copy()
        vg2.move_to(vg1.get_edge_center(RIGHT), LEFT)
        self.play(TransformFromCopy(vg1, vg2))
        self.play(vg2.animate.rotate(-np.pi/2))

        # vg 3
        vg3 = vg2.copy().move_to(vg2.get_edge_center(DOWN), TOP)
        self.play(TransformFromCopy(vg2, vg3))
        self.play(vg3.animate.rotate(-np.pi/2))

        # vg4
        vg4 = vg3.copy().move_to(vg3.get_edge_center(LEFT), RIGHT)
        self.play(TransformFromCopy(vg3, vg4))
        self.play(vg4.animate.rotate(-np.pi/2))

        #center and scale
        vg = VGroup(vg1, vg2, vg3, vg4, a_label1, a_label2, c_label1)
        self.play(vg.animate.center().scale(0.8))
        self.wait()

        # indicate
        self.play(indicatePolygon(vg1[1]), indicatePolygon(vg2[1]), indicatePolygon(vg3[1]), indicatePolygon(vg4[1]))

        # shift
        self.play(vg.animate.scale(0.6).to_edge(LEFT))

        # formulae
        f1 = Tex('c^2=4\\frac{ a^2 }{ 2 }')
        self.play(Write(f1))
        self.wait()
        f2 = Tex('c^2=2a^2')
        self.play(TransformMatchingTex(f1, f2))
        self.wait(3)
        f3 = Tex('c=\\sqrt{2a^2}')
        self.play(TransformMatchingTex(f2, f3))
        self.wait(3)
        f4 = Tex('c=a\\sqrt{ 2 }')
        self.play(TransformMatchingTex(f3, f4))
        self.wait()
        
class PythagoreanTheoremTrigonometry(Scene):
    def construct(self):
        f1 = Tex('{a^2}', '+', '{b^2}', '=', '{c^2}')
        self.play(Write(f1))
        self.wait(3)
        self.play(Indicate(f1[4]))
        self.wait()
        f2 = Tex('(', 'a^2', '+', 'b^2', ')', '\\frac{ 1 }{ c^2 }' '=', '\\frac{c^2}{c^2}')
        self.play(TransformMatchingTex(f1, f2))
        self.wait()
        f3 = Tex( '\\frac{a^2}{c^2}', '+', '\\frac{b^2}{c^2}', '=', '\\frac{c^2}{c^2}')
        self.play(TransformMatchingTex(f2, f3))
        self.wait()
        f4 = Tex( '\\frac{a^2}{c^2}', '+', '\\frac{b^2}{c^2}', '=', '1')
        self.play(TransformMatchingTex(f3, f4))
        f5 = Tex( '(\\frac{a }{c})^2', '+', '(\\frac{b }{c })^2', '=', '1')
        self.play(TransformMatchingTex(f4, f5))
        self.wait()
        self.play(Indicate(f5[0]))
        self.wait()
        self.play(Indicate(f5[2]))
        self.wait(3)
        f6 = Tex('\\cos^2(\\alpha)', '+', '\\sin^2(\\alpha)', '=', '1')
        self.play(TransformMatchingTex(f5, f6))
        self.wait()
