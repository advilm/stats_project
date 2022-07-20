from manim import *
import animation.scenes.sorting as sorting
import animation.scenes.boxplots as boxplots

class Title(Scene):
    def construct(self):
        title = Text("Analyzing Runtime of Sorting Algorithms")
        title2 = Text("in the Real World")
        authors = Text("By: Adil Mohiuddin, Leyna Diep")

        VGroup(title, title2, authors).arrange(DOWN)

        self.play(FadeIn(title, title2))
        self.play(FadeIn(authors, shift=DOWN))

        self.wait()

        self.play(FadeOut(title, title2, authors))

class All(Scene):
    def construct(self):
        Title.construct(self)
        sorting.Sorting.construct(self)
        boxplots.UnsortedBoxplot.construct(self)
