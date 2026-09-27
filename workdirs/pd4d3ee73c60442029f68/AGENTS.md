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

A specialized biological research facility is monitoring a colony of organisms over a period of 3031 days, indexed from day $n=0$ to $n=3030$. The population of the colony on any given day $n$ is represented by a positive integer $a_n$. Due to the specific reproductive and mortality rates of the species, the laboratory has determined that the population follows a strict growth law: for every day $n$ from 0 to 3028, twice the population on day $n+2$ is exactly equal to the sum of the population on day $n+1$ and four times the population on day $n$.

Mathematically, this relationship is expressed as $2 a_{n+2} = a_{n+1} + 4 a_{n}$.

The researchers are investigating the genetic markers of these organisms, which are tied to powers of 2. They want to identify a universal property that holds true regardless of the initial starting populations $a_0$ and $a_1$ (provided they are positive integers and all subsequent $a_n$ remain integers).

Find the largest integer $k$ such that, for any sequence of populations satisfying these conditions, there must be at least one day $n \in \{0, 1, 2, \ldots, 3030\}$ where the population $a_n$ is divisible by $2^k$.

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
