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

In the coastal territory of Arcania, three watchtowers—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular defensive perimeter. The distance between Alpha and Bravo is exactly 34 leagues, the distance between Bravo and Charlie is 15 leagues, and the distance between Alpha and Charlie is 35 leagues.

A specialized communication satellite, designated $\Gamma$, orbits such that its ground-track forms a perfect circle. This circle is designed to have the smallest possible radius that still passes directly over tower Alpha and remains tangent to the straight-line supply road connecting towers Bravo and Charlie.

As the circular path of $\Gamma$ is mapped across the territory, it crosses the straight-line path between Alpha and Bravo at a secondary relay point $X$. Similarly, the path crosses the straight-line path between Alpha and Charlie at a secondary relay point $Y$.

Regional surveyors extend a straight signal beam originating at point $X$ and passing through point $Y$. This beam continues until it intersects the Great Outer Boundary—a massive circular wall that passes through all three watchtowers (Alpha, Bravo, and Charlie). This intersection point beyond $Y$ is designated as Point $Z$.

If the distance from tower Alpha to Point $Z$ is expressed as a fraction $\frac{p}{q}$ in simplest form (where $p$ and $q$ are relatively prime positive integers), calculate the value of $p + q$.

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
