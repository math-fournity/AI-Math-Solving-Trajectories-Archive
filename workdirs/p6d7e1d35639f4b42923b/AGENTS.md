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

A high-tech manufacturing floor is divided into a vast open plane containing 16 specialized docking terminals. These terminals are arranged such that no three terminals lie on a single straight path. 

The facility has been assigned 16 automated mobile robots to occupy these terminals. The robots come in 8 distinct models, with exactly 2 robots of each model (two Model 1s, two Model 2s, and so on, up to two Model 8s). To ensure operational safety and prevent collisions, the facility manager must establish "data links" between the two robots of the same model. Specifically, for every model $k$ (where $k = 1, 2, \ldots, 8$), a physical wireless transmission beam is projected in a straight line segment between the two terminals occupied by the robots of Model $k$.

Safety regulations dictate a strict non-interference protocol: for any two different models $i$ and $j$ ($1 \le i < j \le 8$), the transmission beam connecting the Model $i$ pair must not intersect the transmission beam connecting the Model $j$ pair.

Let $N$ be the number of distinct ways to assign the 16 robots to the 16 terminals such that this non-interference protocol is satisfied. Note that the value of $N$ depends on the spatial layout of the terminals. Calculate the smallest possible value of $N$ across all valid terminal arrangements.

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
