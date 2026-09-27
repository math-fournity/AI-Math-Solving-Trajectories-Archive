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

A specialized irrigation system is being designed for a triangular vineyard defined by three main access gates: North Gate ($A$), West Gate ($B$), and East Gate ($C$), where the distances from $A$ to $B$ and $A$ to $C$ are unequal. 

A circular maintenance track is laid out such that it passes through the North Gate ($A$). This track crosses the western boundary path ($AB$) at a service station $M$ and the eastern boundary path ($AC$) at a service station $N$. The track also intersects the southern boundary path ($BC$) at two specific water valves, $Q$ and $P$, positioned such that valve $Q$ lies between the West Gate ($B$) and valve $P$.

The landscape architects have established three specific geometric constraints for the system's efficiency:
1. A pipeline connecting station $M$ to valve $P$ must run perfectly parallel to the eastern boundary path $AC$.
2. A pipeline connecting station $N$ to valve $Q$ must run perfectly parallel to the western boundary path $AB$.
3. The ratio of the distance from the West Gate to valve $P$ ($BP$) relative to the distance from the East Gate to valve $Q$ ($CQ$) must be exactly equal to the ratio of the lengths of the two boundary paths, $AB$ and $AC$ (i.e., $\frac{BP}{CQ} = \frac{AB}{AC}$).

Based on these structural requirements, calculate the interior angle of the vineyard at the North Gate ($\angle BAC$).

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
