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

In a sprawling city grid containing $n$ distinct subway stations, numbered 1 through $n$, the Department of Transportation decides to automate the transit system. They assign a single outbound destination to each station by choosing a function $f: \{1, \ldots, n\} \rightarrow \{1, \ldots, n\}$ uniformly at random from all $n^n$ possible configurations. Under this system, if a passenger is at station $x$, the only available train will take them directly to station $f(x)$.

Once the system is established, a commuter is placed at a starting location, Station 1. Simultaneously, an inspector is assigned to a target location, Station $a$, which is chosen uniformly at random from the set of all $n$ stations.

The city council will approve the transit map only if the layout allows for a "mutual connection" between these two specific locations. Specifically, there must exist a number of train segments $b \ge 1$ such that a passenger starting at Station 1 eventually reaches Station $a$, and there must also exist a number of train segments $c \ge 1$ such that a passenger starting at Station $a$ eventually travels back to Station 1.

Find the probability that the randomly generated transit map and the randomly selected station $a$ satisfy this mutual connection requirement.

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
