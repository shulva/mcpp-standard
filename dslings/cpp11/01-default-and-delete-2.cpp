// mcpp-standard: https://github.com/Sunrisepeak/mcpp-standard
// license: Apache-2.0
// file: dslings/cpp11/01-default-and-delete-2.cpp
//
// Exercise/练习: cpp11 | 01 - default and delete | 禁止函数重载
//
// Tips/提示: 修复编译器错误, 删除错误的函数调用
//
// Docs/文档:
//   - https://en.cppreference.com/w/cpp/language/function#Function_definition
//   - https://en.cppreference.com/w/cpp/language/function#Deleted_functions
//
// Auto-Checker/自动检测命令:
//
//   d2x checker default-and-delete-2
//

#include <d2x/common.hpp>

#include <iostream>

void func(int x) {
    std::cout << "x = " << x << std::endl;
}

// 显式删除float参数的重载
void func(float) = delete;

int main() {

    func(1);     // int
    //func(1.1f);  // float ->注释掉不被允许的函数调用

    //D2X_WAIT

    return 0;
}