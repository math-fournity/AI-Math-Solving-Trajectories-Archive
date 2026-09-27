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

In a futuristic city, engineers are designing automated courier networks on square grids of size $n \times n$, where coordinates range from $(1, 1)$ at the southwest corner to $(n, n)$ at the northeast corner. In these networks, a "Quantum Drone" moves exclusively like a chess knight. 

A security protocol requires placing "Signal Jammers" on certain grid cells. For a given grid size $n$, the corners $(1, 1)$ and $(n, n)$ are always kept clear of jammers. A configuration of jammers is considered "Secure" if every possible path a Quantum Drone could take from $(1, 1)$ to $(n, n)$ contains at least one cell occupied by a jammer.

A grid dimension $n$ is classified as "Resilient" if, for every possible Secure configuration of jammers, there must exist at least one set of three consecutive stations along the main diagonal—specifically at coordinates $(i, i), (i+1, i+1),$ and $(i+2, i+2)$—where at least two of those three stations are occupied by jammers.

Calculate the sum of all "Resilient" grid dimensions $n$ within the inclusive range $4 \le n \le 100$.

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
