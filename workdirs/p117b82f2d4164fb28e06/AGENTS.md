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

A specialized architectural firm is designing a complex of structures on a flat terrain. Three observation towers—Tower A, Tower B, and Tower C—are positioned such that the straight-line distance between A and B is 3 kilometers, between A and C is 5 kilometers, and between B and C is 7 kilometers.

The firm plans to install a subterranean utility hub, Hub E, at a location exactly symmetric to Tower A across the straight boundary line formed by the path between Tower B and Tower C. A straight fiber-optic cable is laid starting from Tower B, passing through Hub E, and extending until it hits a point D on the perimeter of a circular bypass road that perfectly connects Towers A, B, and C.

To manage the safety of the site, a security station, Station I, is placed at the equidistant center of the triangular zone formed by Tower A, Tower B, and Point D (specifically, the center of the circle that is tangent to all three boundaries of triangle ABD).

A survey is conducted to measure the alignment between the utility hub, the original tower, and the security station. It is found that the square of the cosine of the angle formed at Hub E by the lines connecting to Tower A and Station I (calculated as $\cos^2 \angle AEI$) is equal to a simplified fraction $\frac{m}{n}$. 

Determine the value of $m+n$.

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
