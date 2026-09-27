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

A specialized telecommunications network is being designed for a futuristic city. The network consists of $n$ high-altitude drones and $n$ ground-based relay stations, where $n$ is an integer such that $3 \le n \le 2000$.

The physical connections (fiber-optic cables) are laid out in the shape of an $n$-prism:
- The $n$ drones are connected in a single loop, forming the top $n$-gonal base.
- The $n$ relay stations are connected in a corresponding loop, forming the bottom $n$-gonal base.
- Each drone is connected to exactly one relay station directly below it, forming $n$ vertical support cables.

Engineers must assign one of three distinct frequency channels (Red, Blue, or Green) to each of the $3n$ cables in the network. To prevent signal interference and ensure redundancy, the following two protocols must be strictly followed:
1. For every closed loop in the network that defines a face of the prism (the drone loop, the relay loop, and each of the $n$ rectangular segments between adjacent vertical cables), all three frequency channels must be represented among the cables forming that loop.
2. At every connection point (each of the $2n$ vertices), the three cables that meet there must each be assigned a different frequency channel.

Let $S$ be the set of all possible values of $n$ within the range $3 \le n \le 2000$ for which a valid frequency assignment exists. Find the number of elements in $S$.

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
