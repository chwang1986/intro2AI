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

### 1.2 模板继承链

所有页面必须按这个链继承：

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
- 不要覆盖页面骨架、响应式、主内容区样式

---

## 二、侧边栏约定

### 2.1 sidebar_menu 块的内容规范

**正确写法：**

```html
{% block sidebar_menu %}
<ul class="sider-menu">
  <li><a href="/" class="active">教程首页</a></li>
  <li><a href="/step1">01 标题</a></li>
</ul>
{% endblock %}
```

**常见错误：**

```html
<!-- 错误：缺少 <ul class="sider-menu"> 包裹 -->
{% block sidebar_menu %}
  <li><a href="/">首页</a></li>
{% endblock %}
```

后果：列表项没有 `list-style: none`，文字贴边，padding/margin 全部失效。

### 2.2 sidebar_brand 块

覆盖时保留 `display: flex; align-items: center; gap` 的结构，只替换 SVG 和文字：

```html
{% block sidebar_brand %}
  <svg ...></svg>
  <span style="font-weight:600;font-size:16px;">你的标题</span>
{% endblock %}
```

---

## 三、视觉约定

### 3.1 间距

- 侧边栏内边距：`padding: 10px 24px`（水平 24px 是硬性规定，不能改小）
- 卡片内边距：`padding: 20px ~ 24px`
- 模块间距：`margin-bottom: 24px ~ 32px`
- 文字行高：`line-height: 1.5 ~ 1.75`

### 3.2 颜色使用

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

### 3.3 字体

- 全局字体：`Alibaba PuHuiTi 2.0`（已内嵌在 system_base.html）
- 代码字体：`JetBrains Mono`（通过 design-tokens.css）
- 字号层级：正文 16px > 小字 14px > 辅助 12px

---

## 四、组件使用速查

### 4.1 按钮

```html
<button class="btn btn-primary">主按钮</button>
<button class="btn btn-ghost">次要按钮</button>
<button class="btn btn-text">文字按钮</button>
```

### 4.2 卡片

```html
<div class="card">
  <div class="card-header">标题</div>
  <div class="card-body">内容</div>
</div>
```

### 4.3 标签

```html
<span class="tag tag-brand">蓝色标签</span>
<span class="tag tag-cyan">青色标签</span>
<span class="tag tag-success">绿色标签</span>
```

### 4.4 提示框

```html
<div class="highlight-box">
  <p>提示内容</p>
</div>
```

---

## 五、新建项目 Checklist

新建一个教程子项目时，逐条检查：

- [ ] `app.py` 配置了 `jinja2.FileSystemLoader`，包含 `design-system` 目录
- [ ] `templates/base.html` 正确继承 `system_base.html`
- [ ] `sidebar_menu` 块内有 `<ul class="sider-menu">` 包裹所有 `<li>`
- [ ] 没有复制 `design-tokens.css`，页面引用了根目录的版本
- [ ] 没有使用硬编码颜色，全部使用 CSS 变量
- [ ] 按钮使用 `.btn` 系列 class，不是手写样式
- [ ] 卡片使用 `.card` 系列 class，不是手写样式

---

## 六、资源来源

| 资源 | 来源 | 许可证 |
|------|------|--------|
| 阿里巴巴普惠体 | 阿里巴巴 | 免费商用 |
| IconPark 图标 | 字节跳动 | Apache-2.0 |
| ECharts 图表 | 百度 | Apache-2.0 |
| unDraw 插画 | unDraw | 开源免费 |

**原则：** 所有视觉资源必须来自中国大陆大厂官方渠道，零版权风险。
