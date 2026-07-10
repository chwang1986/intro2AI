# Python 编程简明教程

## 纲领

本教程面向零基础读者，目标是让读者掌握 Python 编程基础，并理解在 AI 时代如何与 AI 协作开发程序。教程分为四个阶段，从 Python 语法入门到 AI 辅助编程实战，循序渐进。

## 学习目标

1. 掌握 Python 基础语法，能独立编写简单程序
2. 理解 Python 的核心数据结构，能处理日常数据任务
3. 学会调用 AI API，与 AI 模型交互
4. 掌握 Prompt Engineering，让 AI 更准确地理解你的需求
5. 建立人-AI 协作的开发工作流，提升开发效率

## 学习路径

### 第一阶段：Python 基础

| 序号 | 主题 | 核心内容 |
|------|------|----------|
| 01 | Python 是什么 | Python 的特点、环境搭建、Hello World |
| 02 | 变量与类型 | 数字、字符串、布尔值、类型转换 |
| 03 | 控制流 | if/else、for 循环、while 循环、break/continue |

### 第二阶段：组织代码

| 序号 | 主题 | 核心内容 |
|------|------|----------|
| 04 | 函数 | 定义函数、参数、返回值、作用域 |
| 05 | 数据结构 | 列表、字典、元组、集合的用法 |

### 第三阶段：实用技能

| 序号 | 主题 | 核心内容 |
|------|------|----------|
| 06 | 文件与异常 | 读写文件、try/except、常见异常 |
| 07 | 面向对象 | 类、对象、属性、方法、继承 |

### 第四阶段：面向 AI 的编程

| 序号 | 主题 | 核心内容 |
|------|------|----------|
| 08 | 调用 AI API | requests 库、API Key 管理、与 AI 对话 |
| 09 | Prompt 工程 | 指令设计、上下文管理、角色设定 |
| 10 | AI 协作工作流 | 需求拆解、迭代开发、代码审查 |

### 第五阶段：综合实战

| 序号 | 主题 | 核心内容 |
|------|------|----------|
| 11 | 综合实战 | 用 AI 协助从零写一个实用程序 |

## 面向 AI 设计的程序开发学习要点

与传统编程学习不同，面向 AI 时代的编程学习强调以下几点：

1. **理解比记忆重要**：不需要死记所有 API，但要理解概念和逻辑，这样才能向 AI 准确描述需求
2. **模块化思维**：把大问题拆成小模块，每个模块让 AI 单独实现，最后组装
3. **验证能力**：AI 生成的代码需要人工验证，要学会写测试用例
4. **迭代沟通**：与 AI 协作不是一次性任务，需要多轮对话来精化结果
5. **安全意识**：AI 可能生成有安全风险的代码，要懂得审查和过滤

## 技术实现

- 框架：Flask (Python)
- 模板：Jinja2
- 样式：自包含 CSS（设计令牌系统）
- 字体：阿里普惠体（免费商用）
- 端口：5003

## 示例脚本

每个学习阶段都配有独立的示例脚本，位于 `examples/` 目录下的对应子文件夹中。每个脚本都可以单独运行：

```bash
cd examples/step1
python3 01_hello.py
python3 02_calculator.py
```

| 阶段 | 示例脚本 | 说明 |
|------|----------|------|
| step1 | `01_hello.py`, `02_calculator.py` | print 用法、四则运算 |
| step2 | `01_variables.py`, `02_type_conversion.py`, `03_string_ops.py` | 变量、类型转换、字符串操作 |
| step3 | `01_if_else.py`, `02_for_loop.py`, `03_while_loop.py` | 条件判断、循环 |
| step4 | `01_define_function.py`, `02_parameters.py`, `03_return_values.py` | 函数定义、参数、返回值 |
| step5 | `01_list_ops.py`, `02_dict_ops.py`, `03_set_tuple.py` | 列表、字典、集合、元组 |
| step6 | `01_read_file.py`, `02_write_file.py`, `03_try_except.py` | 文件读写、异常处理 |
| step7 | `01_class_basics.py`, `02_inheritance.py` | 类基础、继承 |
| step8 | `01_mock_api.py`, `02_api_with_key.py` | 模拟 API 调用、API Key 管理 |
| step9 | `01_structured_prompt.py`, `02_few_shot.py` | Prompt 构建、Few-shot 示例 |
| step10 | `01_modular_ai.py` | 模块化 AI 协作 |
| practice | `todo_cli.py` | 完整命令行待办事项程序 |

## 启动方式

```bash
./start.sh
```

浏览器访问 http://localhost:5003
