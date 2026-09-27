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

A specialized aerospace engineering firm is designing a triangular satellite formation, where three satellites occupy positions $A$, $B$, and $C$. The formation must not be right-angled, and the internal angles of the triangle ($\angle A, \angle B, \angle C$) must be represented by positive integers in degrees. A central monitoring station is located at $O$, the circumcenter of the triangle $ABC$.

The formation is classified as "stable" if it meets three specific geometric navigation constraints:

(a) There exists a signal relay point $P$ on the segment $AB$ (where $P$ is distinct from $A$) such that the circular transmission path passing through $P, O,$ and $A$ is tangent to the line of sight $BO$.
(b) There exists a signal relay point $Q$ on the segment $AC$ (where $Q$ is distinct from $A$) such that the circular transmission path passing through $Q, O,$ and $A$ is tangent to the line of sight $CO$.
(c) The combined length of the communication links $AP, PQ,$ and $QA$ must be at least as long as the sum of the distances of the primary outer boundaries $AB$ and $AC$.

Calculate the total number of unique ordered triples of integer angles $(\angle A, \angle B, \angle C)$ that result in a stable satellite formation.

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
