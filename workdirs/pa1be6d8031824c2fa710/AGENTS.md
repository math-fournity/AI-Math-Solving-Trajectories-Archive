# Solver Task

You are a mathematical problem solver. Solve the problem completely.
Do not search for this exact problem, its official answer, or its solution.
You may use computation for exploration or verification.

Output your complete proof directly in your response (in this TUI).
Do NOT write any files — do not use write/edit tools.
End your proof with a line containing exactly: ### PROOF COMPLETE
Your full reasoning and output are automatically captured by the system.

## Answer Leak Self-Check (MANDATORY before solving)

Before you start solving, check the problem text below for any leaked answers, solutions, solution sketches, or formalization notes that would give away the answer or proof strategy.

If you find ANY of the following in the problem text, do NOT solve the problem. Instead output exactly:
### ANSWER LEAK DETECTED: <brief description of what leaked>

Then stop. Do not attempt to solve a problem whose answer has been leaked.

Watch for:
- Phrases like "The proof follows...", "solution sketch", "Formalization notes"
- Official solutions or answer values embedded in the problem statement
- Lean theorem statements that reveal the answer (e.g. `determine SolutionSet := {n | ...}`)

## Problem

# Problem

In a vast desert, a telecommunications company is planning to install $n$ long-distance fiber optic cables. These cables are laid out in "general position," meaning that no two cables are parallel to each other and no three cables ever cross at the same exact junction point. These cables partition the desert into several distinct maintenance zones (the regions or faces formed by the arrangement).

The company now needs to construct a straight access road that cuts across the entire desert. This road is positioned such that it never passes directly through any junction where two cables cross. As the road travels across the desert, it passes through a specific set of maintenance zones.

The "infrastructure cost" of a single maintenance zone is defined as the number of straight cable segments that form its boundary. To calculate the total maintenance overhead, the company needs to sum the infrastructure costs of every zone that the access road intersects. (Note: If a cable segment serves as a border between two different zones that the road passes through, it is counted twice—once for each zone).

Let $E(n)$ be the maximum possible total infrastructure cost of all such zones intersected by the road. Given that $E(n)$ can be expressed as a linear function $C \cdot n$ for large $n$, find the value of the constant $C$.

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出（必须用英文原文，不要翻译成中文）：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说（必须用英文原文）：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
