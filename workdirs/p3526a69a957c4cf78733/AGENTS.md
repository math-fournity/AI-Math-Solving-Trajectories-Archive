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

In the global telecommunications network of "Aetheria," there are $n$ distinct server hubs. Any two hubs are connected by at most one direct fiber-optic cable. The network is designed with high redundancy: even if all cables connected to any single hub are severed, the remaining network remains fully connected, allowing data to travel between any two surviving hubs.

The Network Authority is testing a new "Directional Flow Protocol." For any two specific hubs, $A$ and $B$, the Authority selects a set of at most $k$ cables and assigns them a fixed, permanent direction of data flow. After these $k$ cables are fixed, a "Worst-Case Stress Test" occurs: an adversary assigns a fixed direction to every single remaining cable in the network.

A cable $l$ is considered "Optimally Accessible" for the pair $(A, B)$ if there exists a path starting at $A$, passing through cable $l$, and ending at $B$, such that the path follows all assigned directions and never visits the same hub twice. 

We say hub $A$ is "$k$-directionally linked" to hub $B$ if, after the Authority chooses their $k$ directions, every cable $l$ in the entire network becomes Optimally Accessible, regardless of how the adversary directs the remaining cables.

If the network configuration is such that every hub $A$ must be $k$-directionally linked to every other hub $B$, what is the minimum value of $k$ that guarantees this property for any network satisfying the redundancy condition?

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
