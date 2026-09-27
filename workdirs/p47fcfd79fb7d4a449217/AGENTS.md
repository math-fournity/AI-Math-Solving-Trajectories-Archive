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

In a futuristic city, an architect is designing a series of rectangular server farms. Each server farm is defined by a grid of cooling units $S_{m,n}$ arranged in $m$ rows and $n$ columns, where $m$ and $n$ are integers between 2 and 10 inclusive ($2 \leq m, n \leq 10$). The units are spaced exactly one meter apart horizontally and vertically.

The architect wants to connect all $mn$ units using a single fiber-optic cable that forms a "loop circuit" $P$. This circuit must satisfy three strict engineering constraints:
1. The cable must form a simple closed polygon with its vertices located at the coordinates of the cooling units.
2. Every single cooling unit in the $m \times n$ grid must lie somewhere on the perimeter of the cable.
3. To maintain signal integrity, every turn in the cable must be exactly $90^{\circ}$ (either a left or right turn), and every straight segment of cable between two consecutive vertices must have a length of exactly $1$ meter or $3$ meters.

We define the feasibility of a server farm $f(m, n) = 1$ if such a cable loop can be constructed for a grid of size $m \times n$, and $f(m, n) = 0$ if it is impossible to satisfy the constraints.

Calculate the total number of feasible server farm configurations by finding the value of:
$$\sum_{m=2}^{10} \sum_{n=2}^{10} f(m, n)$$

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
