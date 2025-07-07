// mcpp-standard: https://github.com/Sunrisepeak/mcpp-standard
// license: Apache-2.0
// file: dslings/cpp11/01-default-and-delete-0.cpp
//
// Exercise/练习: cpp11 | 01 - default and delete | 显示指定构造函数生成行为
//
// Tips/提示: 根据编译器提示使用`= default`和`= delete`修复错误
//
// Docs/文档:
//   - https://en.cppreference.com/w/cpp/language/function#Function_definition
//   - https://en.cppreference.com/w/cpp/language/function#Deleted_functions
//
// Auto-Checker/自动检测命令:
//
//   d2x checker default-and-delete
//

#include <d2x/common.hpp>

#include <iostream>

// default和delete显式控制 -> 编译器默认构造函数的生成行为
struct A { };
struct B {
    B() = default;
    B(int x) { std::cout << "B(int x)" << std::endl; }
};
struct C {
    C() = delete;
    C(int x = 1) { std::cout << "C(int x = 1)" << std::endl; }
};

int main() { // 不要直接修改main函数中的代码

    A a;
    B b;
    C c(1);

    //DhX_WAIT

    return 0;
}