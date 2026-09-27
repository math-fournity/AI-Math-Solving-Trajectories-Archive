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

A high-security digital vault uses a verification protocol based on 1007 encrypted keys, labeled $n = 1, 2, \dots, 1007$. Each key possesses a specific energy signature, $a_n$, calculated by the formula $a_n = 10^n + 10^{2016-n}$ units. All security calculations within the vault are performed under a modular system using the prime number 2017, where 10 is known to be a primitive root.

To unlock the vault, an operator must identify four distinct sets of keys, $S_1, S_2, S_3,$ and $S_4$, defined by the following resonance conditions:
- $S_1$ contains all indices $n$ where $a_n \equiv 1 \pmod{2017}$.
- $S_2$ contains all indices $n$ where $a_n^2 \equiv 2 \pmod{2017}$.
- $S_3$ contains all indices $n$ where $a_n^3 - 3 a_n \equiv 1 \pmod{2017}$.
- $S_4$ contains all indices $n$ where $a_n^3 + a_n^2 - 2 a_n \equiv 1 \pmod{2017}$.

The master bypass code is the sum of every unique index $n$ that belongs to at least one of these four sets (the sum of the elements in $S_1 \cup S_2 \cup S_3 \cup S_4$). Find the value of this master bypass code.

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
