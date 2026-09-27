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

In the city of Arithmos, two logistics managers, Alice and Bob, are tasked with decommissioning a cargo shipment of $n$ identical containers, where $n$ is a two-digit natural number. The decommissioning process follows a strict protocol of partitioning:

1.  **Alice's Opening Move:** Alice begins by splitting the initial $n$ containers into two separate piles, $x$ and $y$, such that $x + y = n$. Both $x$ and $y$ must be natural numbers.
2.  **Sequential Partitioning:** Starting with Bob, the managers take turns selecting any single pile currently containing more than one container and splitting it into two smaller piles of natural numbers (e.g., if a pile has $z$ containers, it is split into $u$ and $v$ where $u+v=z$).
3.  **The Inequality Rule:** To prevent symmetry, the protocol forbids splitting any pile into two equal halves. If a pile contains an even number of containers, it cannot be divided into two identical quantities.
4.  **Winning Condition:** The process continues until every pile consists of exactly 1 container. The last manager to successfully perform a legal split wins the contract, while the manager unable to make a move loses.

Determine the sum of all possible two-digit values of $n$ for which Bob has a winning strategy, ensuring he can claim the contract regardless of how Alice chooses to split the initial $n$ containers.

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
