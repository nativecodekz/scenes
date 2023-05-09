from manimlib import *
import numpy as np

class Scene0(Scene):
    def construct(self):
        f1 = Tex("(", "a", "+", "b", ")", "\\times ", "c", "=", "a", "c",  "+", "b", "c")
        txt1 = Text("Распределительный закон умножения")
        group = VGroup(f1, txt1).arrange(DOWN, buff=1)
        self.play(Write(f1))
        self.wait(3)
        self.play(Write(txt1))
        self.wait(10)
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
        texB = Tex("b")
        texA.next_to(rect1.get_edge_center(UP), UP)
        texB.next_to(rect2.get_edge_center(UP), UP)
        vg += texA
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