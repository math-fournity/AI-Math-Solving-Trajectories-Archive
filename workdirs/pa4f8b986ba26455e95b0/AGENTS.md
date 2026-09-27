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

In the high-tech logistics hub of Neo-Tokyo, a systems engineer is designing a complex routing network. There are $n$ distinct districts in the city, and the engineer must schedule a series of cargo transfers between them.

The engineer plans to create $k$ unique "Dispatcher" profiles and $k$ unique "Receiver" profiles. Each Dispatcher profile $M_i$ (where $1 \leq i \leq k$) and each Receiver profile $N_j$ (where $1 \leq j \leq k$) is represented by an $n \times n$ grid of real-valued efficiency coefficients.

When a Dispatcher profile $M_i$ is paired with a Receiver profile $N_j$, the system generates a combined operational matrix by calculating the standard matrix product $M_i N_j$. The $n$ values located on the main diagonal of this resulting matrix represent the "synchronization levels" for each of the $n$ city districts.

The network protocol requires a specific safety condition: for any pair of indices $i$ and $j$, there must be at least one district among the $n$ districts where the synchronization level is exactly zero if and only if the Dispatcher profile and the Receiver profile have different indices (i.e., $i \neq j$). Conversely, if a Dispatcher and Receiver have the same index ($i = j$), all $n$ synchronization levels on the diagonal must be non-zero.

Given the fixed number of districts $n$, what is the maximum number of unique profile pairs $k$ that the engineer can design while satisfying this safety condition?

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
