from manim import *
import scenes

class All(Scene):
    def construct(self):
        scenes.opening.Opening(self)
        scenes.sorting.Sorting.construct(self)
        scenes.boxplots.UnsortedBoxplot.construct(self)
