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

A specialized logistics company uses a modular container system to transport sensitive electronics. The system uses two types of components: "Outer Casings" (denoted by `(`) and "Inner Plugs" (denoted by `)`). For a shipping configuration to be structurally "Balanced," every Casing must have a corresponding closing Plug.

The company's automated sorting robot uses a specific simplification protocol $\mathcal R$ to verify the integrity of these configurations. The robot is programmed to replace certain patterns with a "Solidified Block" (denoted by `A`) using only the following three rules:
1.  A nested set of two casings and two plugs `(())` can be collapsed into a single `A`.
2.  A single `A` enclosed by a casing and a plug `(A)` can be collapsed into a single `A`.
3.  Two adjacent `A` blocks `AA` can be merged into a single `A`.

A configuration is deemed "Protocol-Valid" if the robot can reduce the entire sequence to a single `A` using any sequence of these three rules. 

However, the protocol $\mathcal R$ is functionally incomplete. There are several structural configurations that are perfectly "Balanced" (meaning they follow the standard mathematical definition of balanced parentheses) but are not "Protocol-Valid" because the robot cannot reduce them to a single `A`.

Find the number of such "Balanced" configurations of length 14 (consisting of 7 casings and 7 plugs) that cannot be reduced to a single `A` by the robot.

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
