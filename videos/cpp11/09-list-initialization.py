import sys, os
from manim import *

"""
Manim Community v0.18.1
manim -pql videos/cpp11/09-list-initialization.py
manim -pqh videos/cpp11/09-list-initialization.py
"""

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from d2x import *

class ListInitialization(MovingCameraScene):
    def construct(self):

        title, logo = mcpp_video_start(self, "{ 列表初始化 }")

        self.wait(0.5)

        self.play(Transform(title, Text("{ ? }", t2c = { '?': PURE_RED })))

        self.wait(0.5)

        # 场景1: 统一代码风格
        self.play(Transform(title, Text("{ 1 - 统一代码风格 }", t2c = { '风格': BLUE })))

        self.wait(0.5)

        code_init_1 = self.create_code_helper("""int a1;
int a2 = 1;
int a3(2);
int a4[3] = { 1, 2 };
""")
        code_init_2 = self.create_code_helper("""int a1 { };
int a2 { 1 };
int a3 { 2 };
int a4[3] { 1, 2 };
""")
        code_init_2.scale(0.85).shift(RIGHT * 3)

        self.play(ReplacementTransform(title, code_init_1))

        self.wait(0.5)

        self.play(
            Transform(code_init_1, code_init_1.copy().scale(0.85).shift(LEFT * 3)),
            ReplacementTransform(code_init_1.copy(), code_init_2),
        )

        self.wait(0.5)

        # 场景2: 避免窄化精度丢失
        title = Text("{ 2 - 避免窄化精度丢失 }", t2c = { '窄化': BLUE })
        self.play(ReplacementTransform(
            VGroup(code_init_1, code_init_2),
            title
        ))

        self.wait(0.5)

        code_init_3 = self.create_code_helper("""int a1 = 1.2;""")
        code_init_4 = self.create_code_helper("""int a3[3] { 1, 2.2, b };""")

        self.play(ReplacementTransform(title, code_init_3))

        self.wait(0.5)

        self.play(DHighlight(VGroup(*code_init_3.code[0][10:12])))

        self.wait(0.5)

        self.play(ReplacementTransform(code_init_3, code_init_4))

        self.wait(0.5)

        select_box = SurroundingRectangle(
            code_init_4.code[0][15:18],
            color=PURE_RED,
            buff=0.1,
        )

        select_box_2 = SurroundingRectangle(
            code_init_4.code[0][20],
            color=YELLOW,
            buff=0.1,
        )

        self.play(Create(select_box))

        self.wait(0.5)

        self.play(Transform(select_box, select_box_2))

        self.wait(0.5)

        code_init_5 = self.create_code_helper("""double b = 3.3;""")
        code_init_6 = self.create_code_helper("""constexpr double b = 3.3;""")

        code_init_5.next_to(code_init_4, UP * 2).scale(0.85)
        code_init_6.next_to(code_init_4, UP * 2).scale(0.85)

        self.play(ReplacementTransform(select_box, code_init_5))

        self.wait(0.5)

        self.play(DHighlight(code_init_4.code[0][20], scale_factor=1.5))

        self.wait(0.5)

        self.play(ReplacementTransform(code_init_5, code_init_6))

        self.wait(0.5)

        self.play(DHighlight(code_init_4.code[0][20], color=PURE_RED, scale_factor=1.5))

        self.wait(0.5)

        # 场景3: 避免窄化精度丢失
        title = Text("{ 3 - 提高容器初始化的简洁性 }", t2c = { '容器初始化': BLUE })
        self.play(ReplacementTransform(
            VGroup(code_init_4, code_init_6),
            title
        ))

        self.wait(0.5)

        code_init_7 = self.create_code_helper("""int arr[] = {1, 2, 3, 4, 5};
std::vector<int> v(arr, arr + sizeof(arr) / sizeof(int));""")
        code_init_8 = self.create_code_helper("""std::vector<int> v {1, 2, 3, 4, 5};""")


        self.play(ReplacementTransform(title, code_init_7))

        self.wait(0.5)

        self.play(DHighlight(code_init_7.code[1][30:], scale_factor=1.5))

        self.wait(0.5)

        self.play(ReplacementTransform(code_init_7, code_init_8))

        self.wait(0.5)

        code_init_9 = self.create_code_helper("""#include <initializer_list>
std::initializer_list<T>;""")
        code_init_9_q = Text("{ ? }", t2c = { '?': PURE_RED })
        code_init_9.next_to(code_init_8, UP * 2)
        code_init_9_q.next_to(code_init_8, UP * 2)

        self.play(ReplacementTransform(code_init_8.copy(), code_init_9_q))

        self.wait(0.5)

        self.play(ReplacementTransform(code_init_9_q, code_init_9))

        self.wait(0.5)

        def code_init_10_template(code_seg2):
            code_seg1 = """#include <initializer_list>

class MyVector {
public:
    MyVector() = default;
    MyVector(std::initializer_list<int> list) {
        """
            code_seg3 = """
    }
};"""
            return code_seg1 + code_seg2 + code_seg3

        code_init_10 = self.create_code_helper(code_init_10_template(""))

        select_box = SurroundingRectangle(code_init_10.code[5][13:40], buff=0.1)

        self.play(
            #TransformMatchingShapes(code_init_9, code_init_10),
            ReplacementTransform(code_init_9, code_init_10),
            FadeOut(code_init_8)
        )

        self.wait(0.5)

        self.play(Create(select_box))

        code_init_11 = self.create_code_helper("""MyVector v1 {1, 2, 3};
MyVector v2 {1, 2, 3, 4, 5};""")
        code_init_11.shift(DR * 2).scale(0.85)
        select_box.set_opacity(0)

        self.play(ReplacementTransform(select_box, code_init_11))
        self.bring_to_front(code_init_11)

        self.wait(0.5)

        self.play(
            Transform(
                code_init_10,
                self.create_code_helper(code_init_10_template("int size = list.size()"))
            ),
        )

        self.wait(0.5)

        self.play(
            Transform(
                code_init_10,
                self.create_code_helper(code_init_10_template("""int size = list.size()
        for (auto it = list.begin(); it != list.end(); ++it) {

        }""")))
        )

        self.wait(0.5)

        # 场景4: 避免初始化语法陷阱
        title = Text("{ 4 - 避免初始化语法陷阱 }", t2c = { '语法陷阱': BLUE })
        self.play(ReplacementTransform(
            VGroup(code_init_10, code_init_11),
            title
        ))

        self.wait(0.5)

        code_init_12 = self.create_code_helper("""#include <iostream>

struct Object {
    Object() { }
    Object(int x) { }
};

int main() {
    Object obj1(1);
    Object obj2();
}""")

        self.play(ReplacementTransform(title, code_init_12))

        self.wait(0.5)

        select_box = SurroundingRectangle(
            code_init_12.code[8][11:],
            buff=0.05,
        )
        select_box_2 = SurroundingRectangle(
            code_init_12.code[9][11:],
            buff=0.05,
        )

        self.play(DHighlight(select_box))

        self.wait(0.5)

        self.play(DHighlight(code_init_12.code[4]))

        self.wait(0.5)

        self.play(Transform(select_box, select_box_2))

        self.wait(0.5)

        code_init_12_1 = Text("{      };").scale(0.45)
        code_init_12_1.move_to(select_box)
        code_init_12.code[9][11:].set_opacity(0)
        select_box.set_opacity(0)

        self.play(FadeIn(code_init_12_1))

        self.wait(0.5)

        self.play(
            DHighlight(code_init_12_1),
            DHighlight(code_init_12.code[3])
        )

        self.wait(0.5)

        mcpp_video_end(self, logo, VGroup(code_init_12, code_init_12_1))


    @staticmethod
    def create_code_helper(code: str):
        return Code(
            code=code,
            background="",
            language="cpp",
        )

if __name__ == "__main__":
    scene = ListInitialization()
    scene.render()