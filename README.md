# Yuliao Gu Academic Homepage

[![Website](https://img.shields.io/badge/website-online-176b62)](https://yuliaogu0331.github.io)
[![GitHub Pages](https://img.shields.io/badge/deployment-GitHub%20Pages-222222?logo=github)](https://github.com/YuliaoGu0331/YuliaoGu0331.github.io)
[![License](https://img.shields.io/badge/license-MIT-c55a35)](LICENSE)

这是 Yuliao Gu 的个人学术主页源码，基于 Jekyll 和 GitHub Pages 构建。当前版本在 [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) 的基础上重新设计了页面结构、视觉系统和前端运行方式，主要用于展示个人简介、研究方向、论文、荣誉、经历与笔记。

- 在线主页：<https://yuliaogu0331.github.io>
- 默认语言：英文
- 部署分支：`master`

## 当前版本特色

### 学术信息优先的首页

首页按照“个人身份、研究兴趣、教育背景”的顺序组织内容，让访客可以快速理解研究方向和学术经历。论文、荣誉等尚无内容的页面使用明确的空状态，不展示虚构或示例数据。

### 清晰、响应式的视觉系统

- 桌面端采用个人资料侧栏与正文双栏布局。
- 平板和移动端自动切换为单栏结构。
- 移动导航支持点击外部关闭、`Esc` 关闭和正确的 ARIA 状态。
- 支持键盘焦点样式、语义化 HTML 和减少动态效果的系统偏好。
- 使用白色背景、深色正文、青绿色链接和暖色强调，适合长时间阅读。

### 数据驱动的个人资料

个人信息维护在 `_config.yml`，链接类型维护在 `_data/profile_links.yml`。作者资料模板通过一个 Liquid 循环生成联系方式，不需要为桌面端和移动端维护两份重复 HTML。

### 更轻量的前端

当前页面不再依赖 jQuery、Stickyfill、Magnific Popup、FitVids 或旧导航插件。交互统一由约 1 KB 的原生 JavaScript 文件 `assets/js/site.js` 负责，减少了请求体积、运行开销和维护成本。

### SEO 与发布支持

- 根据页面标题和描述生成独立的 `<title>` 与 Open Graph 信息。
- 支持 Google、Bing 和 Baidu 站点验证。
- 支持 Jekyll Sitemap、Feed 和重定向插件。
- 推送到 `master` 后由 GitHub Pages 自动构建和发布。
- 可选启用 Google Scholar 引用数据自动更新。

## 项目结构

```text
.
├── _config.yml                 # 站点、作者、SEO 和 Jekyll 配置
├── _data/
│   ├── navigation.yml          # 顶部导航
│   └── profile_links.yml       # 个人资料链接类型与图标
├── _includes/                  # 导航、作者资料、SEO、脚本等可复用模板
├── _layouts/default.html       # 全站页面外壳
├── _pages/                     # 首页及各内容页面
├── _sass/
│   ├── _academic.scss          # 新版页面布局与内容组件
│   ├── _masthead.scss          # 顶部导航
│   ├── _sidebar.scss           # 个人资料侧栏
│   └── _variables.scss         # 字体、颜色和断点变量
├── assets/
│   ├── css/main.scss           # Sass 入口
│   └── js/site.js              # 原生交互脚本
├── images/                     # 头像、favicon 和其他图片
└── google_scholar_crawler/     # 可选的 Scholar 数据抓取脚本
```

## 内容维护

### 1. 修改站点和个人信息

编辑 `_config.yml`：

```yaml
title: "Yuliao Gu"
description: "Academic homepage description"
url: "https://USERNAME.github.io"
repository: "USERNAME/USERNAME.github.io"

author:
  name: "Your Name"
  avatar: "/images/avatar.png"
  bio: "Your affiliation or research area"
  location: "City, Country"
  email: "name@example.com"
  github: "USERNAME"
  researchgate: "https://www.researchgate.net/profile/..."
```

修改 `_config.yml` 后需要重新启动本地 Jekyll 服务，配置不会在运行期间自动重载。

### 2. 修改首页

首页内容位于 `_pages/about.md`，包含：

- 顶部个人简介和联系按钮
- About me
- Research interests
- Education

首页使用少量语义化 HTML 配合 Markdown，以便精确控制版式。修改研究方向、学位时间或院系信息时直接编辑对应文本即可。

### 3. 修改其他页面

主要页面对应关系如下：

| 页面 | 源文件 | 公开路径 |
| --- | --- | --- |
| 首页 | `_pages/about.md` | `/` |
| Research | `_pages/research.md` | `/research/` |
| Publications | `_pages/publications.md` | `/publications/` |
| Honors & Awards | `_pages/awards.md` | `/awards/` |
| Experience | `_pages/experience/experience.md` | `/experience/` |
| Notes | `_pages/comments/comments.md` | `/comments/` |

新建页面时至少需要提供 Jekyll Front Matter：

```yaml
---
permalink: /example/
title: "Example"
description: "Description used by search engines and link previews."
author_profile: true
---
```

所有可公开访问的条目（包括 publications、honors、experience 和 notes）都应同时提供发布日期：

```yaml
date: 2026-08-26
last_modified_at: 2026-08-26 # 可选：页面后续有实质更新时填写
```

日期统一使用 ISO 格式 `YYYY-MM-DD` 保存，页面显示统一由 `_includes/published-date.html` 渲染为 `Published Month D, YYYY`。`date` 表示首次发布日，不因普通文字修订而改变；有重要更新时才添加或更新 `last_modified_at`。索引页中的条目也必须显示相同的发布日期格式。

新增 publication 或 honors 条目时，可使用以下结构：

```yaml
---
permalink: /publications/example/
title: "Example publication"
date: 2026-08-26
author_profile: true
---

# Example publication

{% include published-date.html date=page.date %}
```

### 4. 修改导航

编辑 `_data/navigation.yml`：

```yaml
main:
  - title: "Research"
    url: /research/
  - title: "Publications"
    url: /publications/
```

导航顺序即 YAML 中的排列顺序。首页入口由左上角姓名标识提供，因此不需要额外添加 `Home` 项。

### 5. 添加个人资料链接

`_data/profile_links.yml` 定义可以显示的链接类型。要启用已经定义的链接，只需在 `_config.yml` 的 `author` 下添加同名字段。例如：

```yaml
author:
  googlescholar: "https://scholar.google.com/citations?user=SCHOLAR_ID"
  orcid: "https://orcid.org/0000-0000-0000-0000"
```

要支持新的平台，在 `_data/profile_links.yml` 中添加配置：

```yaml
- key: linkedin
  label: LinkedIn
  icon: "fab fa-linkedin"
  prefix: "https://www.linkedin.com/in/"
```

随后在 `_config.yml` 中设置 `author.linkedin`。`prefix` 可省略，此时字段值应填写完整 URL。

### 6. 修改头像和图标

- 将头像放入 `images/`，然后更新 `_config.yml` 中的 `author.avatar`。
- favicon 文件位于 `images/favicon-*.png` 和 `images/favicon.ico`。
- 推荐使用正方形头像；页面会自动裁剪为圆形。

## 本地开发

### 环境要求

- Ruby 和 RubyGems
- Bundler `2.3.24`（与 `Gemfile.lock` 一致）
- GCC 与 Make（部分 Ruby gem 需要编译）

首次运行：

```bash
gem install bundler -v 2.3.24
bundle _2.3.24_ install
bundle _2.3.24_ exec jekyll serve --livereload
```

也可以使用仓库脚本：

```bash
bash run_server.sh
```

Windows 可运行：

```bat
run_server.bat
```

服务启动后访问 <http://127.0.0.1:4000>。修改 `_config.yml` 后请停止并重新启动服务。

仅执行生产构建：

```bash
JEKYLL_ENV=production bundle _2.3.24_ exec jekyll build
```

生成结果位于 `_site/`。

## 发布到 GitHub Pages

1. 仓库名称应为 `USERNAME.github.io`。
2. 在 `_config.yml` 中更新 `url` 和 `repository`。
3. 将修改提交并推送到默认发布分支：

```bash
git add <files>
git commit -m "update homepage"
git push origin master
```

4. 在仓库的 **Settings → Pages** 中确认发布源指向 `master`。
5. GitHub Pages 构建完成后访问 `https://USERNAME.github.io`。

## 可选：Google Scholar 引用统计

仓库保留了原模板的 Scholar 抓取能力，但当前页面没有默认展示虚构引用数据。启用时：

1. 从 Scholar 个人页面 URL 获取 `SCHOLAR_ID`。
2. 在 GitHub 仓库 **Settings → Secrets and variables → Actions** 中创建 `GOOGLE_SCHOLAR_ID`。
3. 在 **Actions** 页面启用工作流。
4. 在 `_config.yml` 中设置作者的 `googlescholar` URL。
5. 若需要通过 jsDelivr 读取数据，将 `google_scholar_stats_use_cdn` 设为 `true`；CDN 会带来一定缓存延迟。

工作流会生成引用统计 JSON 并推送到 `google-scholar-stats` 分支。自动化依赖第三方页面结构，若 Scholar 限流或调整页面，任务可能暂时失败。

## 维护约定

- 内容事实优先：没有论文、奖项或经历时保留明确空状态，不使用示例成果。
- 样式优先写入 `_sass/`，不要在 `_includes/head.html` 中添加大段内联 CSS。
- 新的个人平台优先扩展 `_data/profile_links.yml`，不要复制整段 Liquid 条件模板。
- 简单交互优先扩展 `assets/js/site.js`，避免重新引入大型前端运行时。
- 提交前至少运行 `git diff --check` 和 Jekyll 构建。

## 致谢与许可

本项目基于 [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io)，并受到 [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) 与 [Academic Pages](https://github.com/academicpages/academicpages.github.io) 的影响。Font Awesome 和 Academicons 分别遵循其自身许可。

项目代码遵循仓库 [LICENSE](LICENSE) 中的许可条款。感谢 RayeRen、tangjyan 及相关开源项目贡献者。
