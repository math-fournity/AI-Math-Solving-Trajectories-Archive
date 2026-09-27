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

In a remote digital archipelago, there are $n$ distinct data servers labeled $V_1, V_2, \dots, V_n$ (where $n > 3$), arranged such that no three servers sit on the same fiber-optic line. The network administrators are installing direct physical cable links between certain pairs of servers. Two servers $V_i$ and $V_j$ are defined as "linked" if a cable is constructed between them.

Initially, $n$ encrypted data packets $C_1, C_2, \dots, C_n$ are distributed across the servers, with exactly one packet at each server. The packets are not necessarily at their matching numerical server (e.g., packet $C_1$ might start at server $V_3$). 

A "reallocation cycle" is a single operation where you select any subset of the packets and simultaneously move each chosen packet to a linked server. To prevent data corruption, two conditions must be met during a cycle:
1. After the move, every server must still contain exactly one packet.
2. No two packets are allowed to have directly swapped their positions with each other in that single move (i.e., if packet $A$ moves from server $X$ to $Y$, packet $B$ cannot move from $Y$ to $X$ in the same cycle).

A network configuration is called "harmonic" if, regardless of how the packets are initially distributed, it is always possible to return every packet $C_i$ to its corresponding server $V_i$ ($1 \le i \le n$) through a finite sequence of reallocation cycles.

What is the minimum number of cable links required to ensure the network is harmonic?

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
