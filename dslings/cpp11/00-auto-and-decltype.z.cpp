// mcpp-standard: https://github.com/Sunrisepeak/mcpp-standard
// license: Apache-2.0
//
// Exercise/练习: cpp11 | 00 - auto and decltype
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

#include <iostream>
#include <vector>

// 3. 函数返回值类型

auto add_func(int a, double b) -> decltype(a + b) {
    return a + b;
}

template<typename T1, typename T2>
D2X_YOUR_ANSWER minus_func(T1 a, T2 b) -> D2X_YOUR_ANSWER {
    return a - b;
}

int main() {

    d2x_assert_eq(minus_func(1, 2), -1);
    d2x_assert_eq(minus_func(2, 1), 1);
    d2x_assert_eq(minus_func(1, 2.1), -1.1);

    D2X_WAIT

    return 0;
}