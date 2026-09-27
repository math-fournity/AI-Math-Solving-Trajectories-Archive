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

In the industrial sector of Hexapolis, a specialized fiber-optic network is being constructed. The network consists of a set of server hubs connected by data cables. Each hub is connected to either exactly 4 cables or exactly 3 cables. There are $a$ hubs with 4 connections and $b$ hubs with 3 connections, where $a$ and $b$ are positive integers. The network is fully integrated, meaning a signal can travel between any two hubs through the cables.

Engineers are testing a "Multi-Phase Protocol." For this protocol to be active, every cable in the network must be assigned one of four distinct frequencies: Cobalt, Ruby, Emerald, or Void. The assignment must follow two strict operational constraints:
1. For every hub that has exactly 3 connections, the three cables attached to it must either be assigned three different colors (one Cobalt, one Ruby, and one Emerald) or they must all be assigned the color Void.
2. At least one cable in the entire network must be assigned a color other than Void.

Let $c$ be the smallest real number such that, if the ratio of 4-connection hubs to 3-connection hubs ($a/b$) is strictly greater than $c$, the network is guaranteed to support at least one valid assignment for the Multi-Phase Protocol, regardless of how the cables are linked.

Compute the value of $100c$.

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
