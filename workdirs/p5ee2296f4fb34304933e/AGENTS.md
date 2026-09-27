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

In a remote digital frontier, a security architect named Bob and a data packet named Anna are engaged in a strategic battle within a square server grid. The grid consists of all integer coordinates $(m, n)$ such that $|m| \le N$ and $|n| \le N$, where $N$ is an integer between 2 and 100 inclusive. The perimeter of this grid, defined by the lines $x = \pm N$ and $y = \pm N$, constitutes the "Firewall." Any coordinate lying on these four lines is considered a Firewall Node.

The packet, Anna, begins her journey at the origin $(0, 0)$. The game proceeds in rounds, with Bob taking the first turn in every round.

In each of his turns, Bob selects exactly two Firewall Nodes on each of the four boundary lines (a total of 8 nodes per turn) and permanently deletes them, making them inaccessible.

In each of her turns, Anna moves the data packet exactly three steps. A single step consists of moving from a current coordinate $(m, n)$ to an adjacent coordinate $(m \pm 1, n)$ or $(m, n \pm 1)$. 

Anna wins the game if she can successfully move the packet to a Firewall Node that has not been deleted by Bob. Bob wins if he can delete enough nodes to prevent Anna from ever reaching an active Firewall Node, regardless of how many turns the game lasts.

Let $S$ be the set of all possible values of $N$ in the range $1 < N \le 100$ for which Anna has a guaranteed winning strategy. Find the sum of all elements in $S$.

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
