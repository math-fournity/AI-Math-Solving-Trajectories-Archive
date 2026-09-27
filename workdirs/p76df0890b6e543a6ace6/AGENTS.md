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

In a remote territory, there are $n$ distinct monitoring stations $p_1, p_2, \dots, p_n$ positioned such that no three stations lie on the same straight line. To ensure security, each station is assigned a single signal frequency: either "Infrared Red" or "Ultra Blue."

A central network $S$ is composed of several triangular data-exchange circuits, where each circuit connects exactly three stations. The network is constructed with a specific balance requirement: for any two possible communication links that could be formed between any two stations (say the link between $p_i$ and $p_j$, and the link between $p_h$ and $p_k$), the number of triangular circuits in $S$ that utilize the first link as a side must exactly equal the number of triangular circuits in $S$ that utilize the second link as a side.

An "unbalanced circuit" is defined as a triangle in $S$ whose three vertex stations are all assigned the same signal frequency (either all Infrared Red or all Ultra Blue).

Find the smallest positive integer $n$ such that, regardless of how the frequencies are assigned to the $n$ stations, the network $S$ is guaranteed to contain at least two unbalanced circuits.

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
