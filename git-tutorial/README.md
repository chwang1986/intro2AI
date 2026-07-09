# git-tutorial —— 如何使用 Git

这是 Intro2AI 项目的第一个教程子目录，目标是让零基础用户通过浏览器交互式学习 Git 版本控制。

## 教程结构

本教程共 8 个阶段，每个阶段都是一个可访问的网页：

| 阶段 | 页面 | 内容 |
|------|------|------|
| 01 | /step1 | Git 是什么 —— 核心概念（工作区、暂存区、仓库） |
| 02 | /step2 | 初始化仓库 —— git init、工作区与暂存区 |
| 03 | /step3 | 添加与提交 —— git add、git commit、提交信息规范 |
| 04 | /step4 | 查看历史与回退 —— git log、diff、checkout、reset |
| 05 | /step5 | 分支管理 —— git branch、switch、merge、冲突解决 |
| 06 | /step6 | 远程仓库 —— git remote、push、pull、clone |
| 07 | /collab | 多人协作 —— 模拟两人协作环境 |
| 08 | /practice | 综合实战 —— 完整工作流自由练习 |

## 每个页面的统一结构

每个教程页面都按以下四段式组织：

1. **场景** —— 什么时候需要这个操作
2. **要点** —— 核心命令和设计原则
3. **错误** —— 初学者常犯的错误
4. **实例** —— 可交互的命令操作台

## 交互式命令台

step2 到 step6、practice 页面都包含一个真实的命令操作台，连接服务器上的 `workspace/` 目录。你可以：

- 点击按钮执行预设命令
- 在输入框中输入自定义命令（practice 页面）
- 实时查看命令输出
- 使用「重置工作区」按钮恢复初始状态

## 多人协作模拟

/collab 页面模拟了两个人共同开发一个项目的场景：

- 点击「创建协作环境」后，系统自动生成远程仓库和两个本地克隆（collab_a 和 collab_b）
- 左右两个终端分别代表用户 A 和用户 B
- 可以分别执行 push/pull，观察协作效果

## 覆盖的 Git 操作

本教程在案例中覆盖了以下所有常用操作：

| 操作类型 | 具体命令 |
|----------|----------|
| **新建** | git init、touch、mkdir |
| **添加** | git add、git add . |
| **提交** | git commit -m "" |
| **删除** | rm、git rm |
| **更新** | echo >> 文件、修改后 add/commit |
| **回退** | git reset --hard、git checkout |
| **分支** | git branch、git switch、git merge |
| **查看** | git status、git log、git diff |
| **暂存** | git stash、git stash pop |
| **标签** | git tag |
| **远程** | git remote、git push、git pull、git clone |
| **同步** | git pull、git fetch |
| **发布** | git push origin main、git tag |

## 技术实现

- **框架**：Flask（Python）
- **模板**：Jinja2，继承自 design-system
- **样式**：design-tokens.css（共享设计系统）
- **交互**：原生 JavaScript + Fetch API
- **命令执行**：Python subprocess（限制在工作区内）
- **字体**：阿里普惠体（免费商用）

## 启动方式

```bash
./start.sh
```

浏览器访问 http://localhost:5002
