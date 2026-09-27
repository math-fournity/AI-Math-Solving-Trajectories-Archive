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

Three schools compete in a chess tournament, each with five students. The first match is between $a_{1}$ from School $A$ and $b_{1}$ from School $B$. If a player loses, they are immediately eliminated. If a player $x_{i}$ from School $X$ beats a player $y_{j}$ from School $Y$, and there is a player remaining in School $Z$, then School $Z$ sends a player to meet $x_{i}$. If not, then School $Y$ sends a player instead. If there are no students left in both Schools $Y$ and $Z$, the competition ends. Each time a player $x_{i}$ from School $X$ wins, School $X$ gets $10^{i-1}$ points. Let $P_{A}, P_{B}, P_{C}$ be the points of Schools $A, B, C$ at the end. Let $N$ be the number of all possible ordered triples $(P_{A}, P_{B}, P_{C})$. Find the remainder when $N$ is divided by $8$.

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
