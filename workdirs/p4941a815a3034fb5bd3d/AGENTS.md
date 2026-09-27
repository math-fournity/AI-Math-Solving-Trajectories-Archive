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

In the city of Modulo-Port, an automated logistics system processes data packets through a central hub. The system uses a specialized encryption protocol $P(x)$, which is a polynomial with integer coefficients. The protocol transforms an initial security clearance level $x$ into a new level $P(x)$.

The hub operates on a cycle where an initial signal of level 0 is repeatedly processed by the protocol. We denote the signal level after $k$ processing cycles as $P^k(0)$. For example, after 1 cycle the level is $P(0)$, after 2 cycles it is $P(P(0))$, and so on.

A "System Reset" is triggered whenever the signal level $P^k(0)$ becomes a multiple of exactly 2020. The system’s stability is defined by a specific resonance integer $N$. The protocol $P(x)$ is considered "N-Stable" if it satisfies a strict synchronization rule: a System Reset occurs at cycle $k$ if and only if $k$ is a multiple of $N$.

The central administration is searching for the most complex stable configuration. Find the largest integer $N$ in the range $\{1, 2, \ldots, 2019\}$ for which there exists an $N$-Stable polynomial $P(x)$ with integer coefficients.

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
