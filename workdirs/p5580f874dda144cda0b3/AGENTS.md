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

In a specialized digital archive, a master technician is organizing data packets for a high-security server. The server can accommodate data packets represented by specific coordinate addresses $(x, y)$. For a given integer capacity $n$, the possible addresses are restricted such that $x$ and $y$ are integers where $1 \leq x \leq n$ and $0 \leq y \leq n$.

The technician needs to select a collection $S$ of these addresses to store sensitive encryption keys. However, to prevent data corruption via "interference patterns," the technician must ensure that no two distinct addresses $(a, b)$ and $(c, d)$ in the collection $S$ are mathematically "aligned." Two addresses are considered aligned if the squared magnitude of the first address, calculated as $a^2 + b^2$, is a divisor of both the scalar product $ac + bd$ and the cross-influence value $ad - bc$.

Following these security protocols, the technician aims to maximize the number of encryption keys stored in the archive. 

Determine, as a function of $n$, the maximum number of addresses that can be included in the set $S$.

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
