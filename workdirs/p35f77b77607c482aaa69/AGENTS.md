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

A specialized deep-sea submersible is navigating a vertical trench with five depth markers, labeled Level 1 (shallowest) to Level 5 (deepest). The mission's goal is to reach the ocean floor (Level 6) to succeed; however, if the submersible rises above Level 1 (Level 0), it loses signal and the mission fails.

The pilot starts with a standard propulsion thruster that has a 50% chance of pushing the sub deeper one level and a 50% chance of pushing it shallower one level every minute. Additionally, there is a sealed emergency override module. This module contains one of two possible experimental thrusters: a "Heavy-Drive" (which always moves the sub deeper) or a "Light-Drive" (which always moves the sub shallower). There is a 50% probability the module contains the Heavy-Drive and a 50% probability it contains the Light-Drive.

The pilot may break the seal on the module at any time. If the seal is broken, the experimental thruster inside must be used immediately for that minute’s movement. For all subsequent minutes, the pilot can freely choose to use either the experimental thruster or the standard thruster.

Let $S$ be the set of depth levels $n \in \{1, 2, 3, 4, 5\}$ where breaking the seal on the module is part of the optimal strategy to maximize the probability of reaching the ocean floor. Find the sum of the elements in $S$.

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
