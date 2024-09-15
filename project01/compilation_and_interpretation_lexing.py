from manim import *
import manim_helper
import numpy as np

# 编译与解释 - 词法分析：Manim 动态演示动画


class Show(Scene):

    text_loader = manim_helper.TextLoader('script.json')

    def prepare(self) -> None:
        self.objects = self.text_loader.apply_to(self, self.text_loader.load())

        self.sample_code = MarkupText(
            '<span color="yellow">print</span>'
            '<span color="white">(\"</span>'
            '<span color="green">Hello, world</span>'
            '<span color="white">\")</span>'
        )

        self.arrow = Arrow(self.sample_code) \
                        .rotate(PI * 1.5).move_to(self.sample_code.get_left()).shift(DOWN + RIGHT * 0.5).scale(0.8)

        self.title_object = Text(self.title)
        self.subtitle_object = Text(self.subtitle).set_color(PINK).shift(DOWN * 1.5)
        self.lexing_result_caption_object = Text(self.lexing_list_caption).set_color(LIGHT_PINK).shift(RIGHT * 3.5 + UP * 2.5).scale(0.5)

        for a in [attr for attr in dir(self) if attr.startswith('lexing_note')]:
            parts = a.split('_')
            setattr(self, '_'.join(parts[:2] + ['object'] + parts[2:]), Text(getattr(self, a)).shift(DOWN * 2 + LEFT).scale(0.64))

        for i, a in enumerate([attr for attr in dir(self) if attr.startswith('broken')]):
            parts = a.split('_')
            setattr(self, '_'.join([parts[0]] + ['object'] + [parts[1]]), Text(getattr(self, a)).shift(RIGHT * 4 + UP * 2).scale(0.5).shift(i * 0.5 * DOWN).set_color('#33FFFF'))

        self.conclusion_object = MarkupText(
            f'<span color="yellow">词法分析: </span>'
            f'<span color="white">将源代码拆分成一个个</span>'
            f'<span color="red">最小的</span>'
            f'<span color="#00FFFF">有意义的</span>'
            f'<span color="white">要素</span>'
        ).shift(DOWN * 3).scale(0.4)

    def finalize(self) -> None:
        pass

    def run(self) -> None:
        pass

    def construct(self):
        self.prepare()

        self.play(LaggedStart(
                Write(self.title_object),
                Write(self.subtitle_object),
                lag_ratio=0.64
        ))
        self.wait(1)
        self.play(LaggedStart(
            Unwrite(self.subtitle_object),
            Unwrite(self.title_object),
            lag_ratio=0.64
        ))
        self.play(Write(self.sample_code))
        self.play(self.sample_code.animate.shift(LEFT * 3))
        self.play(Write(self.lexing_result_caption_object))
        self.arrow.shift(LEFT * 3)
        self.play(Create(self.arrow))

        self.play(Write(self.lexing_note_object_1))
        self.play(self.arrow.animate.shift(RIGHT))
        self.play(ReplacementTransform(self.lexing_note_object_1, self.broken_object_1))
        self.wait(1)
        self.play(Write(self.lexing_note_object_2))
        self.play(self.arrow.animate.shift(RIGHT * 0.2))
        self.play(ReplacementTransform(self.lexing_note_object_2, self.broken_object_2))
        self.wait(1)
        self.play(Write(self.lexing_note_object_3))
        self.play(self.arrow.animate.shift(RIGHT * 2))
        self.play(ReplacementTransform(self.lexing_note_object_3, self.broken_object_3))
        self.wait(1)
        self.play(Write(self.lexing_note_object_4))
        self.play(self.arrow.animate.shift(RIGHT * 1.5))
        self.play(ReplacementTransform(self.lexing_note_object_4, self.broken_object_4))
        self.wait(1)
        self.play(Write(self.lexing_note_object_5))
        self.play(self.arrow.animate.shift(RIGHT * 0.25))
        self.play(ReplacementTransform(self.lexing_note_object_5, self.broken_object_5))
        self.wait(1)
        self.play(Write(self.lexing_note_object_6))
        self.play(ReplacementTransform(self.lexing_note_object_6, self.broken_object_6))

        self.wait(1)
        self.play(Uncreate(self.arrow))
        self.play(Unwrite(self.sample_code))
        self.wait(0.5)

        self.group = VGroup(
            self.lexing_result_caption_object,
            self.broken_object_1,
            self.broken_object_2,
            self.broken_object_3,
            self.broken_object_4,
            self.broken_object_5,
            self.broken_object_6
        )
        self.play(self.group.animate.scale(1.32))
        self.sur = SurroundingRectangle(self.group)

        self.play(Create(self.sur))
        self.play(AnimationGroup(
            self.group.animate.move_to(np.array([0, 0, 0])),
            self.sur.animate.move_to(np.array([0, 0, 0])))
        )

        self.play(Write(self.conclusion_object))
        self.wait(2)
        self.play(LaggedStart(
            LaggedStart(
                Uncreate(self.group),
                Uncreate(self.sur),
                lag_ratio=0.5
            ),
            Unwrite(self.conclusion_object),
            lag_ratio=1
        ))

        self.wait(1)
        self.finalize()
