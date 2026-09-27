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

A specialized circular observatory, known as Sector O, has a radius of exactly 1 unit. Built into its perimeter are five communication towers—A, B, C, D, and E—positioned at perfectly equal intervals around the circular edge.

Each tower is equipped with a high-powered signal beam that projects a circular arc across the interior of the observatory. The beam from any given tower is centered at that tower's location and sweeps an arc from the position of its two nearest neighbors (for instance, the beam from Tower A is an arc centered at A that spans from Tower E to Tower B).

Inside the observatory, these signal arcs cross paths, creating a series of internal intersection points. We label these five intersection points $A^{\prime}, B^{\prime}, C^{\prime}, D^{\prime},$ and $E^{\prime}$ based on their proximity to the corresponding towers. Specifically, $C^{\prime}$ is the intersection point formed by the crossing of the signal arc originating from Tower B and the signal arc originating from Tower D.

Find $X$, the precise distance between Tower A and the intersection point $C^{\prime}$. You may leave your answer in the form $f(x)$, where $f$ is a trigonometric function and $x$ is an angle in degrees in simplest form.

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
