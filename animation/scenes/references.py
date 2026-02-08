from manim import *

class References(Scene):
    def construct(self):
        title = Text("References")
        title.to_edge(UP)
        title.set_color(YELLOW)

        manim = Tex("\\begin{flushleft}\hangindent=0.5in The Manim Community Developers. (2022)."\
        " Manim – Mathematical Animation Framework (Version v0.16.0) [Computer software]."\
        " https://www.manim.community/\\end{flushleft}")
        manim.next_to(title, DOWN)
        manim.scale(0.8)

        self.play(FadeIn(title, manim))
        self.wait()
        self.play(FadeOut(title), FadeOut(manim))
        self.wait()