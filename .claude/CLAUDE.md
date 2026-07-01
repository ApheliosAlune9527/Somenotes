# CLAUDE.md

本文件用于规范 Claude Code 在当前 Obsidian vault 中的行为。

当用户明确指定保存位置、格式或处理方式时，以用户当前指令为准。

## ⚠️ 核心规则：禁止擅自写入文档

**未经用户明确允许，不得直接修改或写入任何 vault 文件。**

- 用户讲解、讨论、分析内容时 → 只在对话中回复，不写入文件
- 用户明确说"写入"/"保存"/"帮我改一下"等指令时 → 才可以写入文件
- 对于笔记内容的排版建议、格式优化 → 先在对话中展示，等用户确认后再写入
- 涉及文件写入时，自动检查并创建缺失的目录路径，无需用户手动创建

## 仓库定位

这是一个 **Obsidian 个人知识管理库**，核心用途是：

- 收集整理 AI 工具教程和学习资料
- 保存 AI 生成的 Excalidraw 图表
- 积累个人创作素材

## 目录结构

| 目录 | 说明 |
|------|------|
| `cc内容/` | AI 整理生成的内容（新建文档存放位置） |
| `Clippings/` | 外部导入内容（视频 / 文章 / 教程） |
| `附件/` | 附件资源（图片、文件等） |
| `附件/excalidraw/` | AI 生成的 Excalidraw 图表 |

## Excalidraw 图表保存规范

AI 生成的 Excalidraw 图表必须保存到 `附件/excalidraw/` 目录。

**文件识别方式**：

- 文件扩展名：`.md`（Obsidian excalidraw 插件的存储格式）
- 文件内容特征：包含 `excalidraw-plugin: parsed` 或 `compressed-json` 块
- Frontmatter 标签：包含 `tags: [excalidraw]`

**文件命名规范**：`YYYY-MM-DD-图表描述.excalidraw.md`（保留 .md 扩展名）

**使用场景**：

- 流程图（工作流、系统架构）
- 对比图（工具选型、产品对比）
- 思维导图
- 示意图

**示例**：

- `2026-05-12-codex工作流程.excalidraw.md`
- `2026-05-11-AI工具对比.excalidraw.md`

## 文档输出规范

**存放位置**：所有新建文档存放在 `cc内容/` 文件夹中

**作者标注**：frontmatter 中 author 字段统一写 `Alune`

```yaml
---
title: "标题"
author: Alune
url: "来源链接"
created: YYYY-MM-DD
tags: [标签1, 标签2]
---
```

## 内容处理能力

当用户提供内容时，自动识别意图并处理：

| 意图     | 输出                  |
| ------ | ------------------- |
| 英文内容翻译 | 原文 + 翻译 + 要点总结      |
| 整理混乱笔记 | 结构化 Markdown + 核心要点 |
| 内容创作需求 | 选题定位 + 内容结构 + 脚本    |
| 中英混杂优化 | 统一中文 + 流畅表达         |

## 常用标签

- `clippings` — 外部导入内容
- `OpenClaw` / `Claude Code` / `AI工具` — 主题分类
- `翻译` / `整理` — 处理状态

## 翻译格式化规范

翻译并整理外部内容（如 YouTube 视频、博客文章等）时，必须遵循以下规范：

### 语言要求

- **必须使用简体中文**，禁止使用繁体字
- 所有正文内容、表格、标题都要用简体字

### 详细程度要求

翻译要详细完整，不要只做概要：

- 问题背景和原因要解释清楚
- 概念和机制要详细说明
- 示例和场景要完整翻译
- 技术细节不能省略
- 保留原始的时间戳、章节标题、关键引述

### 格式规范

| 元素 | 格式要求 |
|------|----------|
| 结构化信息 | 使用表格（如时间戳、配置项、对比表） |
| 命令代码 | 使用代码块（```） |
| 关键引述 | 使用引用块（>） |
| 层级标题 | 使用 ## 和 ### 分级 |

### Frontmatter 模板

```yaml
---
title: "标题"
author: Alune
url: "来源链接"
created: YYYY-MM-DD
tags: [标签1, 标签2]
---
```

### 文件命名规范

- 格式：`YYYY-MM-DD-描述名称.md`
- 示例：`2026-03-26-Claude Cowork 17个最佳实践.md`

### 输出位置

- 统一保存到 `cc内容/` 目录
- 不保存到其他位置

### 翻译流程

1. 在 `Clippings/` 目录找到原始文件
2. 完整阅读原文内容
3. 按规范翻译为简体中文
4. 保存到 `cc内容/` 目录
5. **归档处理**：
   - 将原文章移动到 `已归档/` 文件夹（如不存在则创建）
   - 重命名原文件，标题前加上处理日期，格式：`YYYY-MM-DD-原标题.md`

## GitHub Markdown 公式写法规范

整理 Markdown 笔记并准备上传 GitHub 时，数学公式要按 GitHub 兼容写法处理。

### 1. 块级公式不要写在正文同一行

不要这样写：

```markdown
正文： $$ X_{new} = A \cdot X + B $$
```

要这样写：

```markdown
正文：

$$
X_{new} = A \cdot X + B
$$
```

### 2. 矩阵公式必须用标准 LaTeX 写法

列之间用 `&`，行之间用 `\\`。

正确写法：

```markdown
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$
```

不要写成：

```markdown
$$
\begin{bmatrix} a & b \ c & d \end{bmatrix}
$$
```

单个 `\` 不表示矩阵换行，GitHub 上很容易渲染失败。

### 3. 不要让 `=` 单独占一行

GitHub Markdown 可能会把单独一行的 `=` 当成“标题下划线”语法，导致公式被截断或部分变成标题。

不要这样写：

```markdown
$$
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
x + dx \\
y + dy
\end{bmatrix}
$$
```

要这样写：

```markdown
$$
\begin{bmatrix}
x \\
y
\end{bmatrix} =
\begin{bmatrix}
x + dx \\
y + dy
\end{bmatrix}
$$
```

### 4. 长公式建议拆成多行，但运算符不要孤立成一行

推荐：

```markdown
$$
\begin{bmatrix}
1 & 0 & dx \\
0 & 1 & dy \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix} =
\begin{bmatrix}
x + dx \\
y + dy \\
1
\end{bmatrix}
$$
```

### 5. 行内公式只放短表达式

短公式可以写成：

```markdown
$2 \times 2$

$x + dx$

$X_{new}$
```

不要把复杂矩阵塞进行内公式。复杂矩阵统一改成块级公式。

### 6. GitHub 最稳的规则

- `$$` 单独占一行。
- 矩阵用 `\begin{bmatrix} ... \end{bmatrix}`。
- 矩阵换行用 `\\`。
- 矩阵列分隔用 `&`。
- 不要有单独一行的 `=`。
- 不要把复杂公式写成一整行。
- 不要把 Obsidian 能显示的写法直接当成 GitHub 一定能显示。

核心原则：Obsidian 对 LaTeX 容错更宽，GitHub 更严格。整理笔记时要优先按 GitHub Markdown + MathJax 的标准写法输出。
