---
permalink: /experience/dislocations
title: "Introductions to Dislocations"
date: 2026-09-24
author_profile: true
---

# Introductions to Dislocations: A note collection

{% include published-date.html date=page.date updated=page.last_modified_at %}

**Introductions to Dislocations** is my structured note collection on dislocation theory in materials science, built while reading the classic textbook *Introduction to Dislocations*. The full notes live in the dedicated repository:

**Introductions to Dislocations** 是我在阅读位错领域经典教材 *Introduction to Dislocations* 过程中整理的结构化学习笔记，完整内容收录于独立仓库：

- **Repository / 仓库**: [YuliaoGu0331/dislocation_learn](https://github.com/YuliaoGu0331/dislocation_learn)
- **Language / 语言**: mainly Chinese narration, with English terms annotated at first occurrence; all mathematics in LaTeX / 以中文叙述为主，专业术语首次出现时附英文名称；数学表达统一使用 LaTeX
- **Coverage / 范围**: Chapters 2–10, keeping the numbering of the original learning material / 收录第 2–10 章，章节编号沿用原学习资料

<hr />

## What the notes cover / 内容涵盖

The notes follow the arc of the theory from single dislocations to macroscopic strength:

笔记沿位错理论的主线展开，从单根位错一直到宏观强度：

1. **Observation of dislocations / 位错的观察**: microscopy, etch pits and decoration, and the scales at which atomistic simulation and dislocation dynamics operate / 显微表征、蚀坑与缀饰，以及原子模拟和位错动力学的尺度与用途。
2. **Movement of dislocations / 位错的运动**: glide, climb and cross-slip; lattice resistance, dislocation velocity, and the Orowan equation / 滑移、攀移与交滑移；晶格阻力、位错速度及 Orowan 方程。
3. **Elastic properties / 位错的弹性性质**: stress fields and energies, the Peach–Koehler force, dislocation interactions, and boundary effects / 位错应力场与能量、Peach–Koehler 力、位错相互作用及边界效应。
4. **Dislocations in FCC crystals / FCC 晶体中的位错**: partial dislocations, extended dislocations, stacking-fault energy, dislocation reactions and locks / 不全位错、扩展位错、层错能、位错反应与位错锁。
5. **Other crystal structures / 其他晶体结构**: HCP, BCC and beyond — how geometry, bonding and ordering reshape dislocation cores and plasticity / HCP、BCC 及其他晶体——几何、键合与有序结构如何改变位错核心和塑性机制。
6. **Dislocation intersections and nodes / 位错交叉与位错结**: forest dislocations, jogs, dipoles and prismatic loops, and the link to work hardening / 森林位错、割阶、偶极子与棱柱环，以及它们与加工硬化的联系。
7. **Origin and multiplication / 位错的起源与增殖**: growth defects and nucleation; Frank–Read sources, climb sources and grain-boundary sources / 生长缺陷与形核；Frank–Read 源、攀移源及晶界源。
8. **Dislocation arrays and crystal interfaces / 位错阵列与晶体界面**: grain-boundary geometry and energy, CSL/DSC descriptions, interfacial migration, twinning, and pile-ups / 晶界几何与能量、CSL/DSC 描述、界面迁移、孪晶与位错塞积。
9. **Strength of crystalline solids / 晶体固体的强度**: thermal activation, yielding, alloy strengthening and work hardening, grain-size effects, and the brittle–ductile transition / 热激活、屈服、合金强化与加工硬化、晶粒尺寸效应及脆–韧转变。

A recurring thread is the connection to atomistic simulation and discrete dislocation dynamics — where the continuum picture ends and the core structure takes over.

贯穿各章的一条线索是位错理论与原子模拟和离散位错动力学的联系——即连续介质图像的边界在哪里、位错核心结构从何处开始主导。

## Core equations / 核心公式

Eight relations run through all chapters, organized along the chain "reaction → energy and force → multiplication and motion → plastic rate → macroscopic strength":

八组关系贯穿各章，按"位错反应 → 能量与受力 → 增殖与运动 → 塑性速率 → 宏观强度"组织：

1. **Burgers vector conservation / 伯格斯矢量守恒**: $\mathbf{b}_1+\mathbf{b}_2=\mathbf{b}_3$ — necessary for any reaction, never sufficient / 任何反应的必要条件，但并不保证反应发生。
2. **Line energy / 位错线能**: $E_{\mathrm{el}}\propto Gb^2\ln(R/r_0)$ — why short lines and small Burgers vectors are favored / 解释了短位错线和较小伯格斯矢量在能量上更有利。
3. **Peach–Koehler force / Peach–Koehler 力**: $\mathbf{f}_{\mathrm{PK}}=(\boldsymbol{\sigma}\cdot\mathbf{b})\times\boldsymbol{\xi}$, with the Schmid resolved shear stress $\tau=\sigma\cos\phi\cos\lambda$ / 配合 Schmid 分切应力关系 $\tau=\sigma\cos\phi\cos\lambda$。
4. **Line tension and obstacle spacing / 线张力与障碍间距**: $\tau_c\approx 2\alpha_{\Gamma}Gb/L$ — the Frank–Read and Orowan bypassing scales / 对应 Frank–Read 源启动与 Orowan 绕过的应力尺度。
5. **Orowan equation / Orowan 方程**: $\dot{\gamma}=\rho_m b\bar v$ — linking mobile density and velocity to plastic rate / 将可动位错密度与平均速度同塑性应变速率直接相连。
6. **Thermal activation / 热激活关系**: $\dot{\gamma}=\dot{\gamma}_0\exp[-\Delta G^*(\tau^*)/k_{\mathrm B}T]$ — how temperature and strain rate shift the required stress / 描述温度与应变速率如何改变所需应力。
7. **Taylor relation / Taylor 关系**: $\Delta\tau_{\rho}=\alpha_{\rho}Gb\sqrt{\rho_f}$ — forest hardening from stored dislocations / 储存的森林位错带来的强化贡献。
8. **Hall–Petch relation / Hall–Petch 关系**: $\sigma_y=\sigma_0+k_y d^{-1/2}$ — grain-size strengthening, with its limits stated honestly / 晶粒细化强化，并明确其适用范围与外推限制。

Each formula is accompanied by its range of validity, sign conventions, and physical meaning rather than bare derivation.

每组公式都尽量给出适用条件、符号约定和物理意义，而非孤立的推导结果。

## Why this project / 为什么做这个笔记

Dislocations are the microscopic origin of plastic deformation; understanding them is what connects macroscopic plasticity to the microscale simulations behind it. Coming from a mechanics background with little materials training, I kept these notes to build that intuition — they are reading notes refined with AI assistance, meant for quick review and orientation. For real depth, the original text is irreplaceable.

位错是塑性变形在微观中的本质原因，理解位错，才能把握宏观塑性变形与各种微观模拟之间的联系。我本科力学出身、缺少材料方面的训练，整理这些笔记正是为了建立这种直觉。笔记由阅读随记结合 AI 整理生成，仅供快速复习回顾或快速了解；想要更深刻的体会，仍建议阅读原文。
