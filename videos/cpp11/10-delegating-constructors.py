import sys, os
from manim import *

"""
Manim Community v0.18.1
manim -pql videos/cpp11/10-delegating-constructors.py
manim -pqh videos/cpp11/10-delegating-constructors.py
"""

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from d2x import *

class DelegatingConstructors(MovingCameraScene):
    def construct(self):

        title, logo = mcpp_video_start(self, "{ 委托构造函数 }")

        self.wait(0.5)

        ctors = VGroup(
            Text("默认构造", color=BLUE).move_to(UL * 3 + LEFT),
            Text("拷贝构造", color=GREEN).move_to(UR * 3 + RIGHT),
            Text("移动构造", color=YELLOW).move_to(DOWN * 3)
        ).scale(0.65)

        for c in ctors:
            self.play(DHighlight(c), run_time=0.5)

        self.wait(0.5)

        question = Text("?", color=RED).scale(5).move_to(ORIGIN)
        question.set_opacity(0.35)

        self.play(ReplacementTransform(ctors, question))
        self.bring_to_back(question)

        self.wait(0.5)

        # 1: 构造逻辑复用
        self.play(
            FadeOut(question),
            Transform(title, Text("{ 1 - 构造逻辑复用 }", t2c = { '复用': BLUE }))
        )

        self.wait(0.5)

        code_account_1 = self.create_code_helper("""class Account {
    string id;
    string name;
    string coin;
public:

    Account(string id_) {
        id = id_;
        name = "momo";
        coin = "0元";
    }

    Account(string id_, string name_) {
        id = id_;
        name = name_;
        coin = "0元";
    }

    Account(string id_, string name_, int coin_) {
        id = id_;
        name = name_;
        coin = std::to_string(coin_) + "元";
    }
};      """)
        
        code_account_1.scale(0.7)
        code_account_1_copy = code_account_1.copy()
 
        self.play(ReplacementTransform(title, code_account_1))

        self.wait(0.5)

        self.play(
            DHighlight(code_account_1.code[9][15:], scale_factor=2),
            DHighlight(code_account_1.code[15][15:], scale_factor=2)
        )

        select_box = SurroundingRectangle(code_account_1.code[20:22])
        select_box.scale(1.1)
        select_box.set_stroke_width(1.5)

        self.wait(0.5)
        self.play(Create(select_box))

        ctor_call_1 = Text("""Account(id_, "momo", "0元");""").scale(0.35)
        ctor_call_2 = Text("""Account(id_, name_, "0元");""").scale(0.35)

        ctor_call_1.next_to(code_account_1.code[8]).shift(LEFT * 2)
        ctor_call_1.set_color(YELLOW)
        ctor_call_2.next_to(code_account_1.code[14]).shift(LEFT * 2)
        ctor_call_2.set_color(YELLOW)

        self.wait(0.5)
        code_account_1.code[7:10].set_opacity(0)
        code_account_1.code[13:16].set_opacity(0)
        self.play(
            ReplacementTransform(select_box, ctor_call_1),
            ReplacementTransform(select_box.copy(), ctor_call_2),
        )

        temp_obj_text = Text("临时对象", color=PURE_RED)
        temp_obj_text.next_to(UP * 0.5 + RIGHT * 3)

        arrow_1 = Arrow(
            ctor_call_1.get_right(),
            temp_obj_text.get_left(),
            max_tip_length_to_length_ratio=0.15,
        )

        arrow_2 = Arrow(
            ctor_call_2.get_right(),
            temp_obj_text.get_left(),
            max_tip_length_to_length_ratio=0.1,
        )

        self.wait(0.5)
        self.play(
            Create(arrow_1), Create(arrow_2),
            FadeIn(temp_obj_text)
        )

        code_account_2 = self.create_code_helper("""class Account {
    string id;
    string name;
    string coin;
public:

    Account(string id_) : Account(id_, "momo") { }

    Account(string id_, string name_) : Account(id_, name_, 0) { }

    Account(string id_, string name_, int coin_) {
        id = id_;
        name = name_;
        coin = std::to_string(coin_) + "元";
    }
};      """)

        code_account_2.scale(0.8)

        self.wait(0.5)
        temp_obj_text.set_opacity(0)
        ctor_call_1.set_opacity(0)
        ctor_call_2.set_opacity(0)
        arrow_1.set_opacity(0)
        arrow_2.set_opacity(0)
        self.play(ReplacementTransform(
            code_account_1, code_account_2,
        ))

        self.wait(0.5)
        self.play(
            DHighlight(code_account_2.code[6][23:47]),
            DHighlight(code_account_2.code[8][38:63]),
        )
        self.wait(0.5)

        # 2: 为什么更方便维护?
        title = Text("{ 2 - 为什么更方便维护 }", t2c = { '方便维护': BLUE })
        code_account_2_copy = code_account_2.copy()
        self.play(ReplacementTransform(
            code_account_2,
            title
        ))

        self.wait(0.5)
        coin_text = Text("元").move_to(UR * 2)
        coin_text.set_color(YELLOW)
        self.play(
            FadeOut(title),
            FadeIn(code_account_1_copy, shift=UP * 2),
            Create(coin_text)
        )

        coin_text_new = Text("原石").move_to(coin_text)
        coin_text_new.set_color(YELLOW)

        self.wait(0.5)
        self.play(ReplacementTransform(coin_text, coin_text_new))

        select_box_1 = SurroundingRectangle(code_account_1_copy.code[9][15:])
        select_box_2 = SurroundingRectangle(code_account_1_copy.code[15][15:])
        select_box_3 = SurroundingRectangle(code_account_1_copy.code[21][39:])

        self.wait(0.5)
        self.play(
            ReplacementTransform(coin_text_new.copy(), select_box_1),
            ReplacementTransform(coin_text_new.copy(), select_box_2),
            ReplacementTransform(coin_text_new, select_box_3)
        )

        self.wait(0.5)
        select_box_1.set_opacity(0)
        select_box_2.set_opacity(0)
        select_box_3.set_opacity(0)
        self.play(
            code_account_1_copy.animate.shift(RIGHT * 3).scale(0.5),
            FadeIn(code_account_2_copy, shift=LEFT * 2)
        )

        code_account_1_copy.set_opacity(0)
        select_box = SurroundingRectangle(code_account_2_copy.code[13][39:])

        self.wait(0.5)
        self.play(Create(select_box))

        coin_text = Text('"原石"', color=PURE_RED).scale(0.45)
        coin_text.move_to(code_account_2_copy.code[13][39:])

        self.wait(0.5)
        self.play(
            FadeIn(coin_text),
            FadeOut(code_account_2_copy.code[13][39:]),
            FadeOut(select_box),
        )

        # 3: 和封装成一个init函数的区别
        title = Text("{ 3 - 和封装成init函数的区别 }", t2c = { 'init函数': BLUE })
        self.play(ReplacementTransform(
            VGroup(code_account_2_copy, coin_text),
            title
        ))

        code_account_3 = self.create_code_helper("""class Account {
    // ...
    init(string id_, string name_, int coin_) {
        id = id_;
        name = name_;
        coin = std::to_string(coin_) + "元";
    }

public:
    Account(string id_) { init(id_, "momo", 0); }
    Account(string id_, string name_) { init(id_, name_, 0); }
    Account(string id_, string name_, int coin_) {
        init(id_, name_, coin_);
    }
};""")
        
        code_account_3.scale(0.85)
        code_account_3.code[1].set_color(PURE_GREEN)

        self.wait(0.5)
        self.play(ReplacementTransform(title, code_account_3))

        self.wait(0.5)
        self.play(DHighlight(code_account_3.code[9][26:48]), run_time = 0.3)
        self.play(DHighlight(code_account_3.code[10][40:61]), run_time = 0.5)
        self.play(DHighlight(code_account_3.code[12][8:]), run_time = 0.7)

        construct_flow = self.create_code_helper("""class Account {
    // ...
public:
    Account(string id_, string name_, int coin_)
        /* : 1 - 成员初始化列表 */
    {
        // 2 - 执行构造函数的函数体
        init(id_, name_, coin_);
    }
};
""")

        construct_flow.code[1].set_color(PURE_GREEN)
        construct_flow.code[4].set_color(PURE_RED)
        construct_flow.code[6].set_color(PURE_RED)

        self.wait(0.5)
        self.play(
            FadeOut(code_account_3),
            FadeIn(construct_flow, shift=UP * 2)
        )

        self.wait(0.5)
        self.play(DHighlight(construct_flow.code[4]))
        self.wait(0.5)
        self.play(DHighlight(construct_flow.code[5:9]))

        mem_init_list = Text(': id { id_ }, name { name_ }, coin { std::to_string(coin_) + "元" }')
        mem_init_list.scale(0.38)
        mem_init_list.set_color(PURE_RED)
        mem_init_list.move_to(construct_flow.code[4])
        mem_init_list.shift(DOWN * 0.05 + LEFT * 0.1)

        self.wait(0.5)
        construct_flow.code[6].set_opacity(0)
        construct_flow.code[7].set_opacity(0)
        self.play(
            FadeIn(mem_init_list),
            FadeOut(construct_flow.code[4]),
        )

        # 4 - 注意事项
        code_account_4 = self.create_code_helper("""class Account {
public:
    Account(string id_)
        : Account(id_, "momo"), coin { "0元" } // error
    {

    }

    Account(string id_, string name_) : Account(id_, name_, 0) { }
    Account(string id_, string name_, int coin_)
        : id { id_ }, name { name_ }, coin { std::to_string(coin_) + "元" }
    { }                                     

};""")
        code_account_4.scale(0.8)

        self.wait(0.5)
        mem_init_list.set_opacity(0)
        self.play(
            ReplacementTransform(
                construct_flow,
                code_account_4
            )
        )

        select_box_1 = SurroundingRectangle(code_account_4.code[3][32:46])
        select_box_2 = SurroundingRectangle(code_account_4.code[10][38:75])

        select_box_1.set_color(PURE_RED)
        select_box_2.set_color(PURE_RED)

        self.wait(0.5)
        self.play(Create(select_box_1))
        self.wait(0.5)
        self.play(ReplacementTransform(
            select_box_1.copy(),
            select_box_2
        ))
        self.wait(0.5)
        self.play(
            FadeOut(select_box_2),
            FadeOut(select_box_1),
            FadeOut(code_account_4.code[3][30:]),
        )

        self.wait(1)

        mcpp_video_end(self, logo, code_account_4)

    @staticmethod
    def create_code_helper(code: str):
        return Code(
            code=code,
            background="",
            language="cpp",
        )

if __name__ == "__main__":
    scene = DelegatingConstructors()
    scene.render()