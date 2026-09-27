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

In a remote digital library, there are two separate data archives, Archive M and Archive N. Initially, Archive M contains a file of size $m$ terabytes and Archive N contains a file of size $n$ terabytes, where $m$ and $n$ are non-negative integers. Two systems architects, Ivan and Nikola, are testing a new data compression protocol. They take turns modifying the archives, with Ivan acting first.

On each turn, the architect must select one of the two archives and reduce the size of its file to a smaller, non-negative integer size. However, there is a security constraint: the new file size must be unique. Specifically, the new size cannot be a value that has ever occupied either archive at any previous point in the session, nor can it be equal to either of the two initial sizes, $m$ or $n$.

The first architect who is unable to select a file size that satisfies these uniqueness constraints loses the session.

Let $S$ be the set of all possible initial pairs of file sizes $(m, n)$ such that $0 \le m, n \le 100$. Calculate the number of pairs $(m, n)$ in $S$ for which Ivan has a guaranteed winning strategy regardless of Nikola's moves.

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
