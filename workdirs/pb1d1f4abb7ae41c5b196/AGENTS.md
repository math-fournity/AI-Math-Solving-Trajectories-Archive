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

In a futuristic circular space station, there are $2n$ docking bays arranged in a perfect circle, where $n$ is an integer such that $3 \le n \le 100$. To manage power distribution, each bay must be assigned a unique identification frequency chosen from the set $\{1, 2, 3, \ldots, 2n\}$. Each frequency must be used exactly once.

The bays are indexed $1, 2, \ldots, 2n$ in clockwise order around the station. Let $a_i$ represent the frequency assigned to the $i$-th bay. The station's power grid is considered "balanced" if the total energy load of any two adjacent bays is exactly equal to the total energy load of the two bays located directly across the center of the station. Specifically, the configuration is balanced if $a_i + a_{i+1} = a_{i+n} + a_{i+n+1}$ for every $i$ from $1$ to $2n$ (where the indices wrap around such that $a_{2n+1} = a_1$, $a_{2n+2} = a_2$, and so on).

Let $S$ be the set of all possible values of $n$ in the range $3 \le n \le 100$ for which such a balanced configuration of frequencies can be achieved. Find the sum of all the integers contained in the set $S$.

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
