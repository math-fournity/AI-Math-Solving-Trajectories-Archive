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

In a remote territory, three supply depots—Alpha, Bravo, and Charlie—form the vertices of a triangular logistics network. To optimize operations, three specialized transit routes have been established:

1.  **The Median Routes:** Three straight supply lines connect each depot to the exact midpoint of the opposite boundary (e.g., from Depot Bravo to the midpoint of the route between Alpha and Charlie). We denote these routes as $m_a$ (facing Depot Alpha), $m_b$ (facing Depot Bravo), and $m_c$ (facing Depot Charlie).
2.  **The Priority Corridors:** Three separate corridors originate from each depot, precisely bisecting the internal angle formed by the paths to the other two depots. These are denoted as $w_a$, $w_b$, and $w_c$ respectively.

Three central coordination hubs have been constructed at the specific intersections of these routes:
*   Hub $P$ is located where priority corridor $w_a$ crosses median route $m_b$.
*   Hub $Q$ is located where priority corridor $w_b$ crosses median route $m_c$.
*   Hub $R$ is located where priority corridor $w_c$ crosses median route $m_a$.

Let $F_1$ represent the total land area enclosed by the triangle formed by the three depots (Alpha, Bravo, and Charlie). Let $F_2$ represent the area of the inner triangle formed by the three coordination hubs ($P, Q,$ and $R$).

As the positions of the depots are moved to different geographical coordinates, the ratio of the total area to the hub area, $\frac{F_1}{F_2}$, fluctuates. Determine the smallest positive constant $m$ that serves as a strict upper bound for this ratio, such that $\frac{F_1}{F_2} < m$ for any possible configuration of the three depots.

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
