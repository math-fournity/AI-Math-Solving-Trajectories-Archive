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

In a remote industrial mining complex, there are exactly 14 specialized loading bays arranged in a strict linear sequence, numbered 1 through 14. An automated transport railcar travels from bay 1 to bay 14, carrying cargo containers between them. Due to structural limits, the railcar has a maximum capacity of $C = 25$ containers at any given time.

A "transport order" is defined by a specific pickup bay $A$ and a specific drop-off bay $B$, where $A < B$. We classify a specific pair of bays $(A, B)$ as "vacant" if, during a full run of the railcar, no container is ever assigned to be picked up at bay $A$ and dropped off at bay $B$.

Let $N$ be the largest integer such that we can always identify $N$ "vacant" pairs of bays $(A_1, B_1), (A_2, B_2), \dots, (A_N, B_N)$ where all $2N$ bay numbers involved are completely distinct from one another. This $N$ must represent the minimum number of such disjoint pairs that must exist regardless of how many or few transport orders are processed, provided the railcar's capacity $C$ is never exceeded.

Find the value of $N$.

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
