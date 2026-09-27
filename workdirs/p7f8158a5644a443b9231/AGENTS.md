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

In the coastal kingdom of Geometria, three watchtowers—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—are positioned such that the distance between Alpha and Bravo is 5 leagues, Bravo and Charlie is 7 leagues, and Charlie and Alpha is 8 leagues. These towers define a triangular territory, and a circular defense perimeter ($\omega$) is drawn to pass exactly through all three towers.

A central Command Hub ($P$) is located within the triangular territory. The signal transmission distances from the towers to the Hub satisfy the ratio $PA: PB: PC = 2: 3: 6$. To extend the kingdom's reach, three signal beams are projected from the towers through the Command Hub until they hit the defense perimeter $\omega$. Specifically:
- The beam starting at $A$ passes through $P$ and hits the perimeter at point $X$.
- The beam starting at $B$ passes through $P$ and hits the perimeter at point $Y$.
- The beam starting at $C$ passes through $P$ and hits the perimeter at point $Z$.

The cartographers need to calculate the area of the triangular region formed by the intersection points $X, Y,$ and $Z$. This area can be expressed in the form $\frac{p \sqrt{q}}{r}$ square leagues, where $p$ and $r$ are relatively prime positive integers and $q$ is a square-free positive integer. 

What is the value of $p+q+r$?

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
