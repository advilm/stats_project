from manim import *


def get_axes(label, x_range):
    ax = Axes(
        x_range=x_range,
        y_range=[0,  2, 1],
        x_axis_config={"numbers_to_include": np.arange(
            x_range[0], x_range[1] + 1, x_range[2])},
        tips=False
    )

    label = Text(label, font_size=24)
    label.rotate(PI / 2)
    label.next_to(ax.y_axis.n2p(1), LEFT)

    axes_label = ax.get_axis_labels(x_label="\mu", y_label="")


    return VGroup(ax, label, axes_label)


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
    outliers = VGroup()
    for mobject in boxplot:
        if mobject.name == "Line" or mobject.name == "Rectangle":
            scene.play(Create(mobject))
        elif mobject.name == "Dot":
            scene.play(GrowFromCenter(mobject), run_time=.5)
        elif mobject.name == "Text":
            outliers.add(mobject)

    scene.play(Write(outliers))


def replace_graph(scene, old_graph, label, new_range, new_data):
    new_ax = get_axes(label, new_range)
    new_plot = get_boxplot(new_ax, new_data, 1, 0.75)
    scene.play(ReplacementTransform(old_graph[0], new_ax),
               FadeOut(old_graph[1], shift=RIGHT * 3), FadeIn(new_plot, shift=RIGHT * 3))
    scene.wait()
    return VGroup(new_ax, new_plot)


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

        bubble_ax = get_axes('Bubble', [800, 1700, 100])
        bubble_ax_plot = get_boxplot(bubble_ax, bubble_sort, 1, 0.75)
        bubble_graph = VGroup(bubble_ax, bubble_ax_plot)
        self.play(Write(bubble_ax))
        draw_boxplot(self, bubble_ax_plot)

        selection_graph = replace_graph(self, bubble_graph, 'Selection',
                                        [575, 595, 5], selection_sort)
        insertion_graph = replace_graph(self, selection_graph, 'Insertion',
                                        [215, 230, 5], insertion_sort)
        heap_graph = replace_graph(self, insertion_graph, 'Heap',
                                   [95, 99, 1], heap_sort)
        merge_graph = replace_graph(self, heap_graph, 'Merge',
                                    [124, 130, 1], merge_sort)
        quick_graph = replace_graph(self, merge_graph, 'Quick',
                                    [80, 83, 1], quick_sort)

        self.play(FadeOut(quick_graph))
        self.wait()


class Transition(Scene):
    def construct(self):
        self.play(FadeOut(self.mobjects))
        self.wait()


class SortedBoxplot(Scene):
    def construct(self):
        selection_sort = {
            "low_q": 496.319,
            "upper_q": 497.249,
            "median": 496.74,
            "min": 495.082,
            "max": 498.595,
            "outliers": [492.869, 494.384, 494.386, 494.744, 494.799, 494.909,
                         494.915, 498.652, 499.225, 499.399, 499.712, 500.848,
                         502.655],
        }

        quick_sort = {
            "low_q": 281.8725,
            "upper_q": 285.0225,
            "median": 283.417,
            "min": 278.253,
            "max": 289.022,
            "outliers": [273.941, 275.993, 276.94, 277.077]
        }

        merge_sort = {
            "low_q": 58.449,
            "upper_q": 59.1349,
            "median": 58.6485,
            "min": 57.8202,
            "max": 60.1374,
            "outliers": [61.3913]
        }

        heap_sort = {
            "low_q":  21.93445,
            "upper_q": 22.59225,
            "median": 22.23135,
            "min": 21.003,
            "max": 23.3924,
            "outliers": [20.9035, 20.9132, 23.6025, 23.6372, 23.6696,
                         23.7356, 23.9435, 24.0476, 24.3529, 24.9226,
                         26.0656]
        }

        bubble_sort = {
            "low_q": 1.21296,
            "upper_q": 1.215785,
            "median": 1.21402,
            "min": 1.21161,
            "max": 1.21984,
            "outliers": [1.22268, 1.22307, 1.22479, 1.23174, 1.23338, 1.234,
                         1.23891, 1.24996, 1.26328, 1.26476, 1.50799]
        }

        insertion_sort = {
            "low_q": 0.780005,
            "upper_q": 0.780475,
            "median": 0.7802465,
            "min": 0.779396,
            "max": 0.78118,
            "outliers": [0.77854, 0.779258, 0.781543, 0.781783, 0.781854,
                         0.782062, 0.782089, 0.782471, 0.782652, 0.829324,
                         0.949045, 0.980058]
        }

        selection_ax = get_axes('Selection', [490, 504, 2])
        selection_plot = get_boxplot(selection_ax, selection_sort, 1, 0.75)
        selection_graph = VGroup(selection_ax, selection_plot)
        self.play(Write(selection_ax))
        draw_boxplot(self, selection_plot)

        quick_graph = replace_graph(self, selection_graph, 'Quick',
                                    [272, 290, 2], quick_sort)

        merge_graph = replace_graph(self, quick_graph, 'Merge',
                                    [56, 62, 1], merge_sort)

        heap_graph = replace_graph(self, merge_graph, 'Heap',
                                   [20, 28, 2], heap_sort)

        bubble_graph = replace_graph(self, heap_graph, 'Bubble',
                                     [1.2, 1.5, 0.1], bubble_sort)

        bubble_zoomed_ax = get_axes('Bubble', [1.2, 1.28, 0.02])
        bubble_zoomed_plot = get_boxplot(
            bubble_zoomed_ax, bubble_sort, 1, 0.75)
        bubble_zoomed_graph = VGroup(bubble_zoomed_ax, bubble_zoomed_plot)
        self.play(ReplacementTransform(bubble_graph, bubble_zoomed_graph))
        self.wait()

        insertion_graph = replace_graph(self, bubble_zoomed_graph, 'Insertion',
                                        [0.7, 1, 0.1], insertion_sort)

        insertion_zoomed_ax = get_axes('Insertion', [0.779, 0.782, 0.001])
        insertion_zoomed_plot = get_boxplot(
            insertion_zoomed_ax, insertion_sort, 1, 0.75)
        insertion_zoomed_graph = VGroup(
            insertion_zoomed_ax, insertion_zoomed_plot)
        self.play(ReplacementTransform(
            insertion_graph, insertion_zoomed_graph))
        self.wait()
        self.play(FadeOut(insertion_zoomed_graph))
        self.wait()
