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

An architect is designing a high-tech server farm consisting of a square $10 \times 10$ grid of server racks. Each of the $100$ racks is assigned a unique security clearance level, represented by an integer from $1$ to $100$. The placement of these levels must adhere to two strict physical and logical constraints:

1.  **Cable Constraint:** Any two racks that are physically adjacent (sharing a side) cannot have clearance levels that differ by more than $10$.
2.  **Continuity Constraint:** For any security threshold $k$ (where $k$ is any integer from $1$ to $100$), the group of racks with clearance levels $1$ through $k$ must form a single physically connected cluster (connected via adjacent sides). Simultaneously, the group of racks with clearance levels $k$ through $100$ must also form a single physically connected cluster.

A connection between two adjacent racks is classified as a "High-Stress Link" if the absolute difference between their security clearance levels is exactly $10$. 

The architect wants to minimize the number of High-Stress Links in the entire $10 \times 10$ grid. Let $g(10)$ be this minimum possible number. Find the value of $g(10)$.

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
