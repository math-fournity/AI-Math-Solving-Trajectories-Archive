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

In a remote industrial complex, a circular control panel features a ring of $n$ server modules. Among these, exactly $m$ modules are "Defective," while the remaining modules are "Reliable." Reliable modules always report the true status of the module immediately to their right (clockwise). Defective modules, however, are erratic and can report either "Reliable" or "Defective" regardless of the truth.

A technician arrives to perform maintenance. Their goal is to identify at least one Reliable module to use as a master controller. Upon the technician's arrival, every module simultaneously transmits a single status report to the technician’s terminal, stating whether the module to its immediate clockwise neighbor is "Reliable" or "Defective."

The technician must decide if they can guarantee the identification of a Reliable module based exclusively on these $n$ reports. Let $H(m)$ represent the maximum possible number of Reliable modules that can be present such that the technician still cannot guarantee finding a single Reliable module, regardless of the reports received.

Calculate the value of the following sum:
$\sum_{m=1}^{10} H(m)$

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
