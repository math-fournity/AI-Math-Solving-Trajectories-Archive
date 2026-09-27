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

A specialized digital vault contains a set of unique data crystals. Each crystal has a specific storage capacity measured in terabytes. The vault includes one crystal for every power of two from $2^0$ up to $2^{2023}$ (inclusive). Additionally, the vault contains a single master crystal with a storage capacity of $N$ terabytes, where $N$ is a positive integer that is not a power of two.

The security protocol of the vault is compromised if an "Equilibrium Breach" can occur. An Equilibrium Breach is defined as the ability to select two different collections of crystals from the vault, $A$ and $B$, such that:
1. Both collections $A$ and $B$ contain at least one crystal.
2. The number of crystals in collection $A$ is exactly equal to the number of crystals in collection $B$.
3. The total storage capacity (the sum of the capacities of the crystals) of collection $A$ is exactly equal to the total storage capacity of collection $B$.

Find the smallest possible value for the capacity $N$ such that it is mathematically impossible for an Equilibrium Breach to occur.

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
