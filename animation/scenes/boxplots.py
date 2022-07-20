from manim import *

def get_axes_label(ax, labels):
    label_group = VGroup()
    for i in range(len(labels)):
        label = Text(labels[i], font_size=24)
        label.rotate(PI / 2)
        label.next_to(ax.y_axis.n2p(i + 1), LEFT)
        label_group.add(label)
    return label_group


def get_axes(labels, x_range):
    ax = Axes(
        x_range=x_range,
        y_range=[0, len(labels) + 1, 1],
        x_axis_config={"numbers_to_include": np.arange(
            x_range[0], x_range[1] + 1, x_range[2])},
        tips=False
    )
    labels = get_axes_label(ax, labels)
    return VGroup(ax, labels)


def get_boxplot(ax, data, y, height):
    ax = ax[0]
    min_point = Dot([ax.c2p(data['min'], y)])
    max_point = Dot([ax.c2p(data['max'], y)])
    median_point = Dot([ax.c2p(data['median'], y)])
    low_q_point = Dot([ax.c2p(data['low_q'], y)])
    upper_q_point = Dot([ax.c2p(data['upper_q'], y)])

    box_width = upper_q_point.get_center()[0] - low_q_point.get_center()[0]
    box = Rectangle(width=box_width, height=height * 2)
    box.next_to(low_q_point, RIGHT, buff=0)
    box.shift([-low_q_point.width / 2, 0, 0])

    lower_line = Line(min_point.get_center(), low_q_point.get_center())
    upper_line = Line(upper_q_point.get_center(), max_point.get_center())
    median_line = Line(median_point.get_center() + UP * height,
                       median_point.get_center() + DOWN * height)

    outliers = []
    for x in data['outliers']:
        point = Dot([ax.c2p(x, y)]).get_center()

        asterisk = Text('*')
        asterisk.move_to(point)
        asterisk.set_color(RED)
        asterisk.scale(.75)

        outliers.append(asterisk)

    return VGroup(min_point, max_point, median_point, low_q_point,
                  upper_q_point, lower_line, upper_line, median_line, box, *outliers)


def draw_boxplot(scene, boxplot):
    for mobject in boxplot:
        if mobject.name == "Line" or mobject.name == "Rectangle":
            scene.play(Create(mobject))
        elif mobject.name == "Text" or mobject.name == "Dot":
            scene.play(GrowFromCenter(mobject), run_time=.5)


def replace_graph(scene, old_ax, old_plot, label, new_range, new_data):
    new_ax = get_axes([label], new_range)
    new_plot = get_boxplot(new_ax, new_data, 1, 0.75)
    scene.play(ReplacementTransform(old_ax, new_ax),
               FadeOut(old_plot, shift=RIGHT * 3), FadeIn(new_plot, shift=RIGHT * 3))
    scene.wait()
    return new_ax, new_plot


class UnsortedBoxplot(Scene):
    def construct(self):
        bubble_sort = {
            "low_q": 917.6075,
            "upper_q": 1190.185,
            "median": 1002.08,
            "min": 904.408,
            "max": 1575.84,
            "outliers": [1631.8, 1652.46, 1654.56, 1669.24, 1677.61]
        }

        selection_sort = {
            "low_q": 580.3535,
            "upper_q": 581.614,
            "median": 581.0905,
            "min": 578.576,
            "max": 583.072,
            "outliers": [583.518, 584.493, 586.273, 587.498, 588.189, 590.91],
        }

        insertion_sort = {
            "low_q": 218.632,
            "upper_q": 219.5885,
            "median": 219.0315,
            "min": 217.616,
            "max": 220.891,
            "outliers": [216.757, 221.214, 221.288, 221.355, 221.54, 221.56,
                         221.625, 222.242, 223.86, 224.218, 228.919]
        }

        merge_sort = {
            "low_q": 125.5685,
            "upper_q": 126.137,
            "median": 125.787,
            "min": 124.842,
            "max": 126.981,
            "outliers": [127.099, 127.127, 127.278, 127.4, 128.668, 129.383]
        }

        heap_sort = {
            "low_q": 96.27415,
            "upper_q": 96.50815,
            "median": 96.35195,
            "min": 95.959,
            "max": 96.8516,
            "outliers": [96.91, 96.9648, 97.0292, 97.1825, 97.2452, 98.2989]
        }

        quick_sort = {
            "low_q": 80.7539,
            "upper_q": 80.90075,
            "median": 80.8147,
            "min": 80.5951,
            "max": 81.0937,
            "outliers": [80.4496, 80.527, 81.1568, 81.2081, 81.4157, 82.4489]
        }

        bubble_ax = get_axes(['Bubble'], [800, 1700, 100])
        bubble_ax_plot = get_boxplot(bubble_ax, bubble_sort, 1, 0.75)
        self.play(Write(bubble_ax))
        draw_boxplot(self, bubble_ax_plot)

        selection_ax, selection_plot = replace_graph(self, bubble_ax, bubble_ax_plot,
                                                     'Selection', [575, 595, 5], selection_sort)
        insertion_ax, insertion_plot = replace_graph(self, selection_ax, selection_plot,
                                                     'Insertion', [215, 230, 5], insertion_sort)
        heap_ax, heap_plot = replace_graph(self, insertion_ax, insertion_plot,
                                           'Heap', [95, 99, 1], heap_sort)
        merge_ax, merge_plot = replace_graph(self, heap_ax, heap_plot,
                                             'Merge', [124, 130, 1], merge_sort)
        quick_ax, quick_plot = replace_graph(self, merge_ax, merge_plot,
                                             'Quick', [80, 83, 1], quick_sort)

        self.play(FadeOut(quick_ax, quick_plot))