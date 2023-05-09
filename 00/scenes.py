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
