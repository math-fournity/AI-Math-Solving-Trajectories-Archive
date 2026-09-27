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

In a remote territory, three supply depots—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular logistics network. The straight-line distance between Alpha and Bravo is exactly 13 kilometers, Bravo to Charlie is 14 kilometers, and Alpha to Charlie is 15 kilometers. 

A central maintenance hub, Mike ($M$), is located at the exact midpoint of the road connecting Bravo and Charlie. A circular satellite coverage zone, Gamma ($\Gamma$), is established such that the boundary of the zone passes through Alpha and is perfectly tangent to the road $BC$ specifically at hub Mike. 

Two secondary communication relay towers, Delta ($D$) and Echo ($E$), are positioned where the edge of the coverage zone $\Gamma$ intersects the transport lines $AB$ and $AC$, respectively. A technician identifies a local waypoint, November ($N$), situated at the midpoint of the direct line between towers $Delta$ and $Echo$. 

To optimize signal strength, a new fiber-optic cable is laid along a straight line passing through Mike and November. This cable line intersects the transport line $AB$ at point Papa ($P$) and the transport line $AC$ at point Oscar ($O$). 

The lengths of the segments of this fiber-optic line—specifically the segments $MN$, $NO$, and $OP$—are found to be in a ratio of $a : b : c$, where $a, b, \text{ and } c$ are positive integers with no common divisor greater than 1. Calculate the value of $a + b + c$.

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
