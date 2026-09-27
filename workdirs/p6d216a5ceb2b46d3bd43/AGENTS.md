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

In the competitive world of aerospace engineering, two rival firms, Prime-Tech and Quantum-Aero, have designed distinct propulsion models. Each model is defined by a specific control sequence represented by a sequence of 2021 sequential settings. The "magnitude" of each design is defined by the number of settings, which is 2021 (corresponding to indices from 0 to 2020), and it is known that every single setting for both firms is a non-zero value.

The efficiency of these designs is analyzed through two specific types of "Technical Synchronies":

1.  **Phase Alignments ($r$):** When the control sequences are modeled as continuous functions, the engineers found that the two designs share exactly $r$ real intersection points, taking into account the multiplicity of these points (where the functions meet or stay tangent).
2.  **Modular Matches ($s$):** Upon comparing the 2021 individual settings of Prime-Tech to those of Quantum-Aero, the inspectors found that exactly $s$ of these settings are identical in both value and position.

Given that the two propulsion designs are not identical, determine the maximum possible value for the sum of Phase Alignments and Modular Matches ($r + s$).

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
