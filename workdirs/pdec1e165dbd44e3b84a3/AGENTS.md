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

In the city of Axioma, there are $n$ distinct high-tech sensors, labeled $1$ through $n$. A surveillance agency needs to create a security protocol consisting of an ordered sequence of $n-2$ distinct activation zones, $A_1, A_2, \ldots, A_{n-2}$. Each activation zone $A_k$ is defined as a specific subset of the $n$ sensors.

To ensure the complexity and security of the protocol, the agency mandates two strict operational constraints for any two zones $A_i$ and $A_j$ where $i < j$ (meaning zone $i$ appears earlier in the sequence than zone $j$):

1. The total number of sensors in the earlier zone must be strictly less than the total number of sensors in the later zone (i.e., $|A_i| < |A_j|$).
2. The earlier zone cannot be a complete sub-configuration of the later zone; at least one sensor active in zone $A_i$ must be inactive in zone $A_j$ (i.e., $A_i \not\subseteq A_j$).

How many unique sequences of activation zones $A_1, A_2, \ldots, A_{n-2}$ can be formed that satisfy these requirements?

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
