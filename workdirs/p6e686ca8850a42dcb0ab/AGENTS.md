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

A specialized logistics network is designed as a tiered distribution pyramid where each tier $n$ (for $n \geq 1$) contains $n$ distribution hubs. The operational capacity of these hubs is determined by the following protocol:

1. For any tier $n$, the two "anchor" hubs located at the far left and far right of the row are assigned a capacity equal to $n^2$ units.
2. Every internal hub (those not on the ends) is assigned a capacity equal to the sum of the capacities of the two hubs directly above it in the preceding tier ($n-1$).
3. In the first tier ($n=1$), there is only one hub, which acts as both the left and right anchor, thus having a capacity of $1^2 = 1$.

As an example, in Tier 4, the capacities of the four hubs are $16, 17, 17, \text{and } 16$. In Tier 5, the capacities of the five hubs are $25, 33, 34, 33, \text{and } 25$.

Let $S_n$ represent the total combined capacity of all hubs in Tier $n$. Among the first one million tiers ($1 \leq n \leq 10^6$), for how many values of $n$ is the total capacity $S_n$ exactly divisible by $13$?

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
