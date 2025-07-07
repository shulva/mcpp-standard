// mcpp-standard: https://github.com/Sunrisepeak/mcpp-standard
// license: Apache-2.0
// file: dslings/cpp11/00-auto-and-decltype-0.cpp
//
// Exercise/练习: cpp11 | 00 - auto and decltype | 自动类型推导
//
// Tips/提示: 使用 auto 和 decltype 修复代码中的错误
//
// Docs/文档:
//   - https://en.cppreference.com/w/cpp/language/auto
//   - https://en.cppreference.com/w/cpp/language/decltype
//
// Auto-Checker/自动检测命令:
//
//   d2x checker auto-and-decltype
//

#include <d2x/common.hpp>

int main() {

    // 0. 声明定义
    int a = 1;
    auto a1 = a; // a1 的类型是 int
    int b = 2;
    auto b1 = b;

    decltype(b) b2 = b; // b2 的类型是 int
    decltype(a) a2 = a;

    char c = 'c';
    auto c1 = c;
    decltype(c) c2 = c;

    d2x_assert_eq(a, a1);
    d2x_assert_eq(a1, a2);
    d2x_assert_eq(b, b1);
    d2x_assert_eq(b1, b2);

    //D2X_WAIT

    return 0;
}