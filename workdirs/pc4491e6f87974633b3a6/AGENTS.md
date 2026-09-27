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

In a bustling coastal port, there is a complex logistics network consisting of 2016 unique shipping containers. The containers are organized according to a strict priority protocol: for certain pairs of containers $(A, B)$, container $B$ is "higher-priority" than container $A$. This protocol is transitive, meaning if $B$ is higher-priority than $A$ and $C$ is higher-priority than $B$, then $C$ is higher-priority than $A$. Furthermore, no container is higher-priority than itself.

The port authority needs to organize all 2016 containers into various storage zones. To ensure structural stability and logistical efficiency, every zone must follow one of two strict configurations:
1. **The Parallel Zone:** No container in the zone has a priority relationship with any other container in that same zone.
2. **The Serial Zone:** For every possible pair of containers within the zone, one must be higher-priority than the other.

Let $G$ be the minimum number of storage zones required to accommodate all 2016 containers under these rules. Considering all possible priority protocols that could exist among the 2016 containers, what is the maximum possible value of $G$?

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
