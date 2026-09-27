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

A specialized triangular communications network is established between three main hubs—Alpha (A), Bravo (B), and Charlie (C)—forming an equilateral triangle where each direct link (AB, BC, and CA) has a length of exactly 1 unit.

Along each link, two signal boosters are positioned. On link BC, boosters $A_1$ and $A_2$ are placed such that the distance from Bravo to $A_1$ is less than the distance to $A_2$. On link CA, boosters $B_1$ and $B_2$ are placed such that the distance from Charlie to $B_1$ is less than to $B_2$. On link AB, boosters $C_1$ and $C_2$ are placed such that the distance from Alpha to $C_1$ is less than to $C_2$.

Technical cables are laid connecting three specific pairs of boosters: one cable connects $B_1$ to $C_2$, another connects $C_1$ to $A_2$, and the third connects $A_1$ to $B_2$. It is confirmed that these three cables intersect at a single common junction point.

Maintenance crews monitor three specific triangular service zones formed by the hubs and the boosters: Zone 1 is defined by the boundary $A-B_2-C_1-A$, Zone 2 by $B-C_2-A_1-B$, and Zone 3 by $C-A_2-B_1-C$. Engineers discover that the perimeter (the sum of the three boundaries) of each of these three service zones is identical.

Find all possible values for this common perimeter.

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
