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

In a remote sector of the ocean, three sonar communication stations—Alpha, Bravo, and Charlie—are positioned such that the distance between Bravo and Charlie is 10 kilometers, the distance between Charlie and Alpha is 12 kilometers, and the distance between Alpha and Bravo is 14 kilometers. The three stations form an acute triangle.

Each station projects a circular signal interference zone where the diameter of the zone is the straight-line distance to one of its neighboring stations. Specifically:
- Zone 1 has a diameter equal to the 10 km distance between Bravo and Charlie.
- Zone 2 has a diameter equal to the 12 km distance between Charlie and Alpha.
- Zone 3 has a diameter equal to the 14 km distance between Alpha and Bravo.

At the center of the triangle, there is a "dead zone" region formed by the intersection of all three circular interference zones. The boundary of this mutual intersection consists of three inward-curving arcs. A circular research buoy, $\Omega$, is deployed in this dead zone such that it is internally tangent to these three boundary arcs.

The radius of this research buoy can be expressed in the form $\frac{m-p \sqrt{q}}{n}$ kilometers, where $m, p,$ and $n$ are positive integers with no common prime divisor, and $q$ is a square-free positive integer. 

Compute the value of $m+n+p+q$.

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
