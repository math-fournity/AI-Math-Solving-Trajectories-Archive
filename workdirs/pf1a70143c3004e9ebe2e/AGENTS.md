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

An engineering firm is designing a high-security containment vault. The floor plan is a symmetric trapezoidal hall $ABCD$. The two side walls $AD$ and $BC$, as well as the long front entrance wall $AB$, are all constructed to have the exact same length. The rear emergency wall $CD$ is designed to be shorter than these three walls ($CD < AD$).

Inside this hall, two circular robotic surveillance units, $k_1$ and $k_2$, are deployed. The larger unit, $k_1$, has a footprint radius of $r_1$ and is positioned so that its edge is simultaneously flush against (tangent to) the three walls $AD$, $AB$, and $BC$.

The smaller unit, $k_2$, has a footprint radius of $r_2$. It is positioned further back in the hall such that its edge is flush against the three walls $BC$, $CD$, and $AD$. To optimize coverage, the two units are programmed to maneuver until their outer shells are touching each other at exactly one point (externally tangent).

Under these specific geometric constraints, for any fixed primary radius $r_1$, the secondary radius $r_2$ is uniquely determined by a constant scaling factor $x$, such that $r_2 = r_1 \cdot x$.

Find the value of $1000x^2$, rounded to the nearest integer.

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
