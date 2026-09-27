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

In a specialized digital ecosystem, a single server node begins a recursive replication process every hour. If at hour $n$ there are nodes $a_{1}, \ldots, a_{N}$, then in the following hour, every node $a_{i}$ replicates into four distinct sub-nodes: $a_{i}^{(1)}, a_{i}^{(2)}, a_{i}^{(3)},$ and $a_{i}^{(4)}$.

Data links are established between these nodes according to the following protocol:
1. Two sub-nodes $a_{i}^{(j)}$ and $a_{k}^{(j)}$ (sharing the same index $j$) possess a data link if and only if their parent nodes $a_{i}$ and $a_{k}$ possessed a data link at hour $n$.
2. Every sub-node with index $j$ possesses a data link to every sub-node with index $j+1$ (for $j=1, 2, 3$), regardless of which parent nodes they originated from. This means $a_{i}^{(j)}$ and $a_{k}^{(j+1)}$ are linked for all $1 \leq i, k \leq N$ and $j \in \{1, 2, 3\}$.
3. Data links are symmetric but not transitive (if node A is linked to B, and B is linked to C, A is not necessarily linked to C). No node is linked to itself.

Following this protocol, there is 1 node at hour zero, 4 nodes after 1 hour, 16 nodes after 2 hours, and so on. Analysts are examining the state of the network after 3 hours. They are specifically looking for "unstable clusters," defined as unordered sets of four distinct nodes $\{b_{1}, b_{2}, b_{3}, b_{4}\}$ that contain an odd total number of data links between them. 

What is the total number of such unstable clusters after 3 hours?

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
