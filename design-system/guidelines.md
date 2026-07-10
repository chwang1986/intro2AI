# 前端设计约定 —— 新建项目必读

这份文档记录了我们所有教程/应用项目必须遵守的设计约定。目标是：**让新建项目的样式一眼看去就是"我们家的"，而不是每个项目各自为政。**

---

## 一、项目结构约定

### 1.1 最小文件集合

每个新教程子项目只保留这 4 个文件/目录：

```
<教程名>-tutorial/
├── app.py              # Flask 入口
├── start.sh            # 本地启动脚本
├── README.md           # 项目说明
└── templates/          # HTML 模板
```

**注意：**
- 不要复制 `design-tokens.css`，通过模板继承引用根目录的 `design-system/design-tokens.css`
- 不要新建 `static/css/` 目录放自己的样式，优先用 design-tokens.css 里的工具类
- 如果确实需要 static（如图片），可以保留，但 CSS 仍应通过 system_base.html 引用

### 1.2 模板继承链（强制）

所有页面必须按这个链继承，**不允许跳过**：

```
页面模板 (如 step1.html)
    ↓ extends
子项目 base.html (如 wpt-tutorial/templates/base.html)
    ↓ extends
system_base.html (design-system/system_base.html)
```

**子项目 base.html 的职责：**
- 覆盖 `sidebar_brand`：放项目专属 Logo + 标题
- 覆盖 `sidebar_menu`：**必须包含 `<ul class="sider-menu">` 包裹所有 `<li>`**
- 覆盖 `head`：引入项目专属资源（如 MathJax）
- **不要**覆盖页面骨架、响应式、主内容区样式

---

## 二、侧边栏约定

### 2.1 sidebar_brand 块（必须覆盖）

每个子项目的 base.html **必须**覆盖 sidebar_brand，让用户知道自己在哪个教程里：

```html
{% block sidebar_brand %}
  <svg viewBox="0 0 48 48" fill="none" class="sidebar-icon">...</svg>
  <span class="font-semibold text-lg">你的教程标题</span>
{% endblock %}
```

**注意：**
- 只替换 SVG 和文字，不要改 `.sider-brand` 的样式（padding、height、gap 等由 system_base.html 控制）
- SVG 必须使用 `class="sidebar-icon"`，禁止使用 `style="width:28px;height:28px;color:..."`
- 标题文字必须使用 `class="font-semibold text-lg"`，禁止使用行内 `style`

### 2.2 sidebar_menu 块的内容规范

**正确写法：**

```html
{% block sidebar_menu %}
<ul class="sider-menu">
  <li><a href="/" class="{% if not current_step %}active{% endif %}">
    <span class="step-badge">●</span> 教程大纲
  </a></li>
  {% for step in steps %}
  <li>
    <a href="/{{ step.id }}" class="{% if current_step == loop.index %}active{% endif %}">
      <span class="step-badge">{{ loop.index }}</span>
      {{ step.title }}
    </a>
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

**必须遵守的规则：**
- 外层必须有 `<ul class="sider-menu">` 包裹
- 菜单项使用 `<span class="step-badge">` 显示序号，不要用硬编码 "01"、"02"
- 链接格式统一为 `/step1`（**不带 .html 后缀**）
- active 判断统一用 `current_step` 变量

**常见错误：**

```html
<!-- 错误：缺少 <ul class="sider-menu"> 包裹 -->
{% block sidebar_menu %}
  <li><a href="/">首页</a></li>
{% endblock %}

<!-- 错误：链接带 .html 后缀 -->
<a href="/step1.html">...</a>

<!-- 错误：硬编码序号 -->
<a href="/step1">01 标题</a>
```

---

## 三、路由约定

### 3.1 URL 格式

所有教程的路由必须统一为以下格式：

| 页面 | URL |
|------|-----|
| 首页/大纲 | `/` |
| 步骤页面 | `/step1`, `/step2`, ... |
| 综合实战 | `/practice` |
| 特殊页面 | `/collab` 等，根据需求定 |

**禁止**使用 `.html` 后缀的路由（如 `/step1.html`）。

### 3.2 app.py 模板配置

每个子项目的 app.py 必须配置 jinja2.FileSystemLoader，让模板能找到 system_base.html：

```python
import jinja2

app.jinja_loader = jinja2.FileSystemLoader([
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, '..', 'design-system'),
])
```

---

## 四、内容区块组件

### 4.1 页面标题区

所有 step 页面统一使用 `page-header` 结构：

```html
<div class="page-header">
  <h1>Step N — 标题</h1>
  <p>一句话描述</p>
</div>
```

**不要**在 step 页面中添加 `back-link`（回到首页链接），sidebar 已经有导航了。

### 4.2 内容区块容器

教学内容统一放在 `lesson-section` 中：

```html
<div class="lesson-section">
  <h2>场景</h2>
  <p>...</p>
</div>

<div class="lesson-section">
  <h2>原理</h2>
  <p>...</p>
</div>

<div class="lesson-section">
  <h2>要点</h2>
  <ul>...</ul>
</div>

<div class="lesson-section">
  <h2>常见错误</h2>
  <div class="highlight-box">...</div>
</div>

<div class="lesson-section">
  <h2>练习</h2>
  <div class="exercise-box">...</div>
</div>
```

### 4.3 可用的内容组件

design-tokens.css 已内置以下组件，**优先使用这些 class，不要自己写样式**：

| 组件 | class | 用途 |
|------|-------|------|
| 内容区块 | `.lesson-section` | 教学内容的章节容器 |
| 概念卡片 | `.concept-card` | 原理讲解、概念说明 |
| 提示框 | `.highlight-box` | 重要提示、注意事項 |
| 错误提示 | `.mistake-card` | 常见错误、避坑指南 |
| 练习区 | `.exercise-box` | 课后练习 |
| 演示卡片 | `.demo-card` | 效果展示、代码演示 |
| 公式框 | `.formula-box` | 数学公式居中展示 |
| 代码块 | `<pre><code>` | 代码示例（已统一样式） |

---

## 五、视觉约定

### 5.1 间距

- 侧边栏内边距：`padding: 10px 24px`（水平 24px 是硬性规定）
- 卡片内边距：`padding: 20px ~ 24px`
- 模块间距：`margin-bottom: 24px ~ 32px`
- 文字行高：`line-height: 1.5 ~ 1.75`

### 5.2 颜色使用

| 场景 | 变量 | 说明 |
|------|------|------|
| 页面背景 | `--bg-page: #F5F7FA` | 浅灰，不能用纯白 |
| 卡片背景 | `--bg-card: #FFFFFF` | 纯白 |
| 主标题 | `--text-primary` | 近黑 |
| 副标题/描述 | `--text-secondary` | 灰 |
| 主强调色 | `--color-primary: #1677FF` | 蓝 |
| 成功 | `--color-success: #52C41A` | 绿 |
| 警告 | `--color-warning: #FAAD14` | 黄 |
| 错误 | `--color-error: #F5222D` | 红 |

**禁止：** 硬编码颜色值（如 `#333`、`#666`、`#999`），一律用 CSS 变量。

### 5.3 字体

- 全局字体：`Alibaba PuHuiTi 2.0`（已内嵌在 system_base.html）
- 代码字体：`JetBrains Mono`（通过 design-tokens.css）
- 字号层级：正文 16px > 小字 14px > 辅助 12px

**字号必须通过 CSS 变量使用，禁止硬编码：**

| 级别 | 变量 | px | 用途 |
|------|------|-----|------|
| 超大标题 | `--font-size-4xl` | 38px | 首页 Hero |
| 大标题 | `--font-size-3xl` | 30px | 页面主标题 |
| 标题 | `--font-size-2xl` | 24px | page-header h1 |
| 小标题 | `--font-size-xl` | 20px | section h2 |
| 副标题 | `--font-size-lg` | 18px | 卡片标题、sidebar 品牌 |
| 正文 | `--font-size-md` | 16px | 段落正文 |
| 小字 | `--font-size-sm` | 14px | 描述、辅助文字 |
| 辅助 | `--font-size-xs` | 12px | 标签、脚注 |

**禁止：** `font-size: 15px`、`font-size: 13px`、`font-size: 11px` 等不在上表中的硬编码值。

---

## 六、格式红线（必须遵守）

### 6.1 禁止行内 style 属性

**HTML 模板中禁止使用 `style="..."` 属性。** 所有样式必须通过 CSS class 实现。

**错误：**

```html
<!-- 错误：行内样式 -->
<span style="font-weight:600;font-size:18px;">标题</span>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">...</div>
<p style="margin:0;font-size:14px;color:var(--text-secondary);">...</p>
```

**正确：**

```html
<!-- 正确：使用 CSS 类 -->
<span class="font-semibold text-lg">标题</span>
<div class="grid-2">...</div>
<p class="m-0 text-sm text-secondary">...</p>
```

**唯一例外：** SVG 动画相关的 `style="animation-delay:..."` 可以保留。

### 6.2 禁止旧版 CSS 变量

以下变量名已废弃，**禁止使用**：

| 旧变量 | 新变量 | 说明 |
|--------|--------|------|
| `--spacer-6` | `--space-2` | 8px |
| `--spacer-8` | `--space-2` | 8px |
| `--spacer-12` | `--space-3` | 12px |
| `--spacer-16` | `--space-4` | 16px |
| `--spacer-20` | `--space-5` | 20px |
| `--spacer-24` | `--space-6` | 24px |
| `--radius-sm` | `--border-radius-md` | 8px |
| `--radius-full` | `--border-radius-full` | 9999px |
| `--brand` | `--color-primary` | 主色 |
| `--brand-light` | `--color-primary-bg` | 主色浅背景 |
| `--bg` | `--bg-card` 或 `--gray-2` | 背景 |
| `--surface` | `--gray-2` | 表面色 |
| `--border` | `--border-color` | 边框色 |
| `--text` | `--text-primary` | 主文字色 |

### 6.3 禁止硬编码颜色

**禁止使用十六进制颜色值**，一律使用 CSS 变量：

```html
<!-- 错误 -->
<p style="color:#666;">...</p>
<div style="background:#eaeaea;">...</div>

<!-- 正确 -->
<p class="text-secondary">...</p>
<div style="background:var(--gray-3);">...</div>
```

**SVG 中的颜色例外：** SVG fill/stroke 可以使用设计令牌中的颜色值（如 `#1677FF`），但应保持一致。

---

## 七、组件使用速查

### 7.1 按钮

```html
<button class="btn btn-primary">主按钮</button>
<button class="btn btn-ghost">次要按钮</button>
<button class="btn btn-text">文字按钮</button>
```

### 6.2 卡片

```html
<div class="card">
  <div class="card-header">标题</div>
  <div class="card-body">内容</div>
</div>
```

### 6.3 标签

```html
<span class="tag tag-brand">蓝色标签</span>
<span class="tag tag-cyan">青色标签</span>
<span class="tag tag-success">绿色标签</span>
```

### 6.4 提示框

```html
<div class="highlight-box">
  <p>提示内容</p>
</div>
```

---

## 八、新建项目 Checklist

新建一个教程子项目时，逐条检查：

### 8.1 基础设施

- [ ] `app.py` 配置了 `jinja2.FileSystemLoader`，包含 `design-system` 目录
- [ ] `app.py` 定义了全局 `STEPS` 列表，每个项有 `id`、`title`、`desc`
- [ ] `app.py` 的路由使用 `/step1` 格式（**不带 .html**）
- [ ] `templates/base.html` 继承 `system_base.html`
- [ ] `base.html` 覆盖了 `sidebar_brand`，SVG 使用 `class="sidebar-icon"`，标题使用 `class="font-semibold text-lg"`
- [ ] `base.html` 的 `sidebar_menu` 包含 `<ul class="sider-menu">` 包裹
- [ ] `base.html` 的菜单链接使用 `/step1` 格式，用 `step-badge` 显示序号

### 8.2 内容规范

- [ ] 首页使用 `index.html`，包含学习路线卡片
- [ ] step 页面使用 `page-header` 结构，不添加 `back-link`
- [ ] 教学内容放在 `lesson-section` 中
- [ ] 原理讲解用 `concept-card`，错误提示用 `mistake-card` 或 `highlight-box`
- [ ] 练习区用 `exercise-box`
- [ ] 没有手写样式覆盖系统组件（如按钮、卡片）

### 8.3 格式红线（逐文件检查）

- [ ] **没有行内 `style` 属性**（搜索 `style="` 应返回 0 结果，SVG 动画除外）
- [ ] **没有硬编码字号**（搜索 `font-size: \d+px` 应返回 0 结果）
- [ ] **没有旧版 CSS 变量**（搜索 `--spacer-` / `--brand` / `--radius-sm` 等应返回 0 结果）
- [ ] **没有硬编码颜色值**（搜索 `#\d{3,6}` 在 HTML 中应仅出现在 SVG 内）
- [ ] 字号全部使用 `--font-size-*` 变量或 `.text-xs` / `.text-sm` / `.text-md` 等工具类
- [ ] 间距全部使用 `--space-*` 变量或 `.m-*` / `.p-*` / `.gap-*` 等工具类

### 8.4 资源

- [ ] 按钮使用 `.btn` 系列 class
- [ ] 卡片使用 `.card` 系列 class
- [ ] 代码块使用 `<pre><code>`（已统一样式）
- [ ] 表格使用 design-tokens.css 的表格样式（已统一）

---

## 八、资源来源

| 资源 | 来源 | 许可证 |
|------|------|--------|
| 阿里巴巴普惠体 | 阿里巴巴 | 免费商用 |
| IconPark 图标 | 字节跳动 | Apache-2.0 |
| ECharts 图表 | 百度 | Apache-2.0 |
| unDraw 插画 | unDraw | 开源免费 |

**原则：** 所有视觉资源必须来自中国大陆大厂官方渠道，零版权风险。
