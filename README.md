# mcpp-standard

现代C++标准核心语言特性代码练习 - **动手学现代CPP核心特性**

| [代码/视频列表](videos/README.md) - [论坛](https://forum.d2learn.org/category/20) - [使用说明](book/src/chapter_1.md) |
| --- |

---

## 0.快速开始

> 通过使用[xlings](https://github.com/d2learn/xlings)获取项目并运行**编译器驱动开发模式**(自动化检测)来进行代码练习

<details>
  <summary>点击查看xlings安装命令</summary>

---

#### Linux

```bash
curl -fsSL https://d2learn.org/xlings-install.sh | bash
```

#### Windows - PowerShell

```bash
Invoke-Expression (Invoke-Webrequest 'https://d2learn.org/xlings-install.ps1.txt' -UseBasicParsing).Content
```

> 注: xlings包含所需的xim和d2x工具 -> [详情](https://d2learn.org/xlings)

---

</details>

### 获取项目

> 下载项目到当前目录并自动配置本地环境

```bash
xlings install d2x:mcpp-standard
```

注: 可以在项目目录执行`d2x book`命令, 本地打开使用说明书

### 练习代码自动检测

> 进入项目目录`mcpp-standard`运行checker命令, 进入练习代码自动检测程序

```bash
xlings checker
```

### 指定练习进行检测

```bash
xlings checker [name]
```

> 注: 练习名支持模糊匹配

## 1.练习及视频解读列表

| c++标准 | 特性 | 标题 | 练习代码/视频 | 备注 |
| --- | --- | --- | --- | --- |
| **引导** | `项目使用教程/引导` | hello mcpp | [code](dslings/hello-mcpp.cpp) | |
| **cpp11** | `00 - auto和decltype` | 类型推导 | [code](dslings/cpp11/00-auto-and-decltype-0) / [video](https://www.bilibili.com/video/BV1xkdYYUEyH) | |
| | | decltype注意事项 | [code](dslings/cpp11/00-auto-and-decltype-4.cpp) / [video](https://www.bilibili.com/video/BV1KWoMYUEzW) | [补充](https://forum.d2learn.org/topic/82) |
| | `01 - default和delete` | 控制默认构造函数生成 | [code](dslings/cpp11/01-default-and-delete-0.cpp) / [video](https://www.bilibili.com/video/BV1B35pz5EN2) | |
| | | 类型对象行为控制示例 | [code](dslings/cpp11/01-default-and-delete-1.cpp) / [video](https://www.bilibili.com/video/BV1Vg5tznE8o) | |
| | `02 - override和final` | 重写显示意图和编译器检查 | [code](dslings/cpp11/02-final-and-override-0.cpp) / [video](https://www.bilibili.com/video/BV1BdLJz6EKJ) | |
| | | 继承和重现限制 | [code](dslings/cpp11/02-final-and-override-1.cpp) / [video](https://www.bilibili.com/video/BV1H1jAzTEYT) | |
| | | | | |

## 2.社区 | 交流

- **即时交流(QQ群):** 167535744
- **练习代码/技术交流&讨论:** [论坛版块](https://forum.d2learn.org/category/20)

## 3.参与项目 | 社区贡献

- **参与社区交流:** 反馈问题、参与社区问题讨论
- **参与项目维护和开发:** 参与社区中问题处理、修复Bug、开发&优化新功能/模块