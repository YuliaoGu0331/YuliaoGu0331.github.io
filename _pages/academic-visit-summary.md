---
permalink: /experience/academic-visit-summary
title: "学术访问总结"
author_profile: true
---

# 学术访问与联合研究总结 (2026.04)

<hr />

### Q1：本次学术访问的核心任务和交流地点是什么？

**A：** 本次访问赴相关研究机构开展了为期一周的学术交流。在此期间，我们团队与对方课题组针对**高熵合金（Cantor Alloy）在极端冲击条件下的位错动力学演化与损伤机理**进行了深入的探讨，并共同开展了大规模分子动力学联合模拟计算。

<hr />

### Q2：联合研究取得了哪些具体进展？

**A：** 我们重点对 CoCrFeMnNi 高熵合金在冲击载荷下的剪切带萌生以及堆垛层错（Stacking Faults）的动态演化进行了多尺度分析。通过结合双方的理论模型，我们成功修正了在高应变率下的位错形核临界应力公式。批量数据分析步骤如下：

1. 打开 **OVITO** 软件，导入超过 1000 万原子的冲击模拟轨迹文件；
2. 运行 **Common Neighbor Analysis (CNA)** 识别晶体缺陷；
3. 使用 **Dislocation Extraction Algorithm (DXA)** 提取位错线并计算位错密度。

<hr />

### Q3：在服务器上联合调试 LAMMPS 脚本时，如何批量修复势函数报错？

**A：** 这是多组分势函数文件路径未正确识别导致的。批量修复步骤如下：

1. 在 **运行终端** 中，确认当前执行路径；
2. 检查 LAMMPS 核心脚本中的 `pair_coeff` 偏好设置；
3. 在弹出报错的脚本行中，修改参数为：
   * **Range**: `Whole document`（整篇文档检查）
   * **Potential Type**: <code class="language-plaintext highlighter-rouge">potential.eam.alloy</code>（强制指定多组分势文件）

<hr />

### Q4：下一阶段的合作规划是什么？

**A：** 预计在下个季度完成论文的初稿撰写。主要计划包含以下两点：
* 进一步完善基于机器学习势函数（MLP）的高熵合金高温高压状态方程描述。
* 联合撰写并整理本次模拟的核心数据，预计于今年下半年提交学术论文初稿。