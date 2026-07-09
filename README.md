# Intro2AI

这是我的日常工作与技术学习总仓库。所有编码项目、教程、实验都存放在这里，并同步到 GitHub。

## 仓库定位

- **用途**：个人知识库 + 技术实验场 + 教程发布平台
- **受众**： primarily 我自己，其次是任何对相同主题感兴趣的读者
- **风格**：简洁明快、中文优先、代码可运行、教程可交互

## 项目结构

```
intro2AI/
├── README.md              # 本文件：仓库总纲领
├── todo.md                # 待办事项与进度跟踪
├── push-to-github.sh      # 一键推送脚本
├── design-system/         # 统一设计系统（所有子项目共享）
│   ├── design-tokens.css  # CSS 变量与组件样式
│   └── base.html          # Jinja2 基础模板
└── git-tutorial/          # 教程一：如何使用 Git
    ├── README.md          # 子目录纲领
    ├── app.py             # Flask 应用入口
    ├── start.sh           # 本地启动脚本
    ├── templates/         # HTML 模板
    └── static/css/        # 样式文件
```

## 设计系统

所有教程子项目共享同一套视觉风格：

- **字体**：阿里普惠体（免费商用）
- **颜色**：浅灰背景 + 白卡片 + 蓝色强调
- **组件**：统计卡片、徽章、表格、图表、标签页、开关等
- **规范**：详见 `design-system/design-tokens.css`

## 已有教程

| 目录 | 主题 | 状态 |
|------|------|------|
| `git-tutorial/` | 如何使用 Git | 搭建中 |

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/chwang1986/intro2AI.git
cd intro2AI

# 启动某个教程（以 git-tutorial 为例）
cd git-tutorial
./start.sh
```

## 推送更改

```bash
./push-to-github.sh
```

## 许可证

所有代码与文档采用 MIT 协议。使用的第三方资源（阿里普惠体、ECharts、IconPark）均为免费商用。
