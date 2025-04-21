# mcpp-standard

现代C++标准核心语言特性代码练习 - **动手学现代CPP核心特性**

| [代码/视频列表](videos/README.md) - [论坛](https://forum.d2learn.org/category/20) |
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

| c++标准 | 时间 | 核心语言特性 | 练习代码/视频 | 练习命令 | 备注 |
| --- | --- | --- | --- | --- | --- |
| 引导 | 2025/4/12 | **hello mcpp** | [code](dslings/hello-mcpp.cpp) | `xlings checker hello-mcpp` | 项目使用教程/引导 |
| cpp11 | 2025/4/12 | **00-auto/decltype** | [code](dslings/cpp11/00-auto-and-decltype-0) / [video](https://www.bilibili.com/video/BV1xkdYYUEyH) | `xlings checker auto-and-decltype` | |
| | 2025/4/16 | **+--->** decltype注意事项 | [code](dslings/cpp11/00-auto-and-decltype-4.cpp) / [video](https://www.bilibili.com/video/BV1KWoMYUEzW) | `xlings checker auto-and-decltype-4` | [补充](https://forum.d2learn.org/topic/82) |
| | 2025/4/19 | **01-default/delete** | [code](dslings/cpp11/01-default-and-delete-0.cpp) / [video](https://www.bilibili.com/video/BV1B35pz5EN2) | `xlings checker default-and-delete` | |
| | 2025/4/21 | **+->** 不可拷贝对像 | [code](dslings/cpp11/01-default-and-delete-1.cpp) / [video](https://www.bilibili.com/video/BV1Vg5tznE8o) | `xlings checker default-and-delete-1` | |
| | | | | |

## 2.社区 | 交流

- **即时交流(QQ群):** 167535744
- **练习代码/技术交流&讨论:** [论坛版块](https://forum.d2learn.org/category/20)

## 3.参与项目 | 社区贡献

- **参与社区交流:** 反馈问题、参与社区问题讨论
- **参与项目维护和开发:** 参与社区中问题处理、修复Bug、开发&优化新功能/模块