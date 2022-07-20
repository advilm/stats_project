from manim import *

class Sorting(Scene):
    def construct(self):
        numbers = [Text(str(x)) for x in [6, 3, 2, 5, 4, 1]]
        number_group = VGroup(Text("["), *numbers, Text("]"))
        number_group.arrange(RIGHT)

        self.play(Write(number_group))
        self.wait()

        sorted_numbers = [Text(str(x + 1)) for x in range(len(numbers))]
        sorted_number_group = VGroup(Text("["), *sorted_numbers, Text("]"))
        sorted_number_group.arrange(RIGHT)
        sorted_number_group.shift(DOWN)

        self.play(number_group.animate.shift(UP))

        arrow = Arrow(number_group.get_bottom(), sorted_number_group.get_top())

        arrow_label = Text("???")
        arrow_label.next_to(arrow, RIGHT)

        self.play(Write(sorted_number_group),
                  GrowArrow(arrow), Write(arrow_label))
        self.wait()
        self.play(FadeOut(sorted_number_group, arrow, arrow_label),
                  number_group.animate.shift(DOWN))

        title = Text("Selection Sort")
        title.set_color(YELLOW)
        title.to_edge(UP)

        self.play(Write(title))

        def swapNumbers(ind1, ind2):
            num_one = numbers[ind1]
            num_two = numbers[ind2]
            self.play(num_one.animate.set_color(BLUE),
                      num_two.animate.set_color(BLUE))
            self.play(num_one.animate.shift(UP),
                      num_two.animate.shift(UP))
            self.play(num_one.animate.move_to(num_two.get_center()),
                      num_two.animate.move_to(num_one.get_center()))
            self.play(num_one.animate.shift(DOWN),
                      num_two.animate.shift(DOWN))
            self.play(num_one.animate.set_color(WHITE),
                      num_two.animate.set_color(WHITE))
            numbers[ind1], numbers[ind2] = numbers[ind2], numbers[ind1]

        window = SurroundingRectangle(numbers[0])
        window.set_color(GREEN)
        for i in range(len(numbers)):
            min_index = i
            for j in range(i + 1, len(numbers)):
                if int(numbers[j].text) < int(numbers[min_index].text):
                    min_index = j
            if i != min_index:
                swapNumbers(i, min_index)

            if i == 0:
                self.play(Create(window))
            else:
                new_window = SurroundingRectangle(
                    VGroup(numbers[0], numbers[i]))
                new_window.set_color(GREEN)
                self.play(Transform(window, new_window))

        self.play(FadeOut(window))
        self.wait()
        self.play(FadeOut(title, number_group))
        self.wait()
