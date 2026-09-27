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

A specialized logistics hub handles 100 unique cargo crates, each assigned a distinct priority ranking from 1 to 100. For any specific sequence of 100 crates passing through a processing bay, a technician defines a "ghost exit" as a dummy crate, $a_{101}$, with a priority of 0.

The facility operates under a protocol defined by a fixed integer $k$ (where $1 < k < 100$). A supervisor monitors the first $k$ crates in the sequence and notes their priority levels. He then waits for the first crate appearing later in the sequence (at some position $m$, where $m > k$) that satisfies a "priority bypass" condition: its priority value must be lower than at least $k-1$ of the first $k$ crates. 

Let $N_k$ represent the total number of possible sequences (out of all 100! possible permutations) in which the specific crate that triggers this bypass condition is the crate with priority rank 1.

Your task is to calculate the sum of all possible values of $k$ for which the number of such sequences, $N_k$, is exactly equal to $\frac{100!}{4}$.

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
