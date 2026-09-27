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

A paper equilateral triangle $ABC$ has side length $12$. The paper triangle is folded so that vertex $A$ touches a point on side $\overline{BC}$ a distance $9$ from point $B$. The length of the line segment along which the triangle is folded can be written as $\frac{m\sqrt{p}}{n}$, where $m$, $n$, and $p$ are positive integers, $m$ and $n$ are relatively prime, and $p$ is not divisible by the square of any prime. Find $m+n+p$. 
[asy]
import cse5;
size(12cm);
pen tpen = defaultpen + 1.337;
real a = 39/5.0;
real b = 39/7.0;
pair B = MP("B", (0,0), dir(200));
pair A = MP("A", (9,0), dir(-80));
pair C = MP("C", (12,0), dir(-20));
pair K = (6,10.392);
pair M = (a*B+(12-a)*K) / 12;
pair N = (b*C+(12-b)*K) / 12;
draw(B--M--N--C--cycle, tpen);
draw(M--A--N--cycle);
fill(M--A--N--cycle, mediumgrey);
pair shift = (-20.13, 0);
pair B1 = MP("B", B+shift, dir(200));
pair A1 = MP("A", K+shift, dir(90));
pair C1 = MP("C", C+shift, dir(-20));
draw(A1--B1--C1--cycle, tpen);[/asy]

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
