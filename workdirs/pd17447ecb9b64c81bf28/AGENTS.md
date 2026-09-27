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

In the high-tech logistics hub of Neo-Kyoto, there are exactly $n = 4035$ unique docking bays, indexed from $1$ to $4035$. Every day, a fleet of $4035$ distinct autonomous cargo drones, also labeled $1$ through $4035$, arrives to occupy these bays. Each drone must park in exactly one bay, and no two drones can share a bay. Thus, the daily parking arrangement is always a permutation of the drone IDs across the bays.

The city's security firm, Aegis, deploys "Sentry Protocols." A Sentry Protocol is a fixed parking schedule—a specific permutation of the $4035$ drones across the $4035$ bays. A security overlap is triggered if, for any docking bay $k$, the drone parked in that bay by the daily arrival matches the drone assigned to that same bay $k$ by a Sentry Protocol.

A set $E$ of Sentry Protocols is defined as "Unavoidable" if, no matter how the drones choose to park on any given day, there is always at least one Sentry Protocol in $E$ that triggers a security overlap with that day's arrangement.

Let $m$ be the minimum number of Sentry Protocols required to create an Unavoidable set $E$. Find the value of $m$.

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
