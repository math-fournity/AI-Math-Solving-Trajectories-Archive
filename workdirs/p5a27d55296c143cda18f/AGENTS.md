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

In a specialized circular naval defense zone, denoted by the perimeter $\omega$, three strategic buoys—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—are anchored. The direct distance between buoys Alpha and Bravo is exactly $24$ kilometers, while the distance between Bravo and Charlie is $23$ kilometers. The defense zone's radius is exactly $15$ kilometers.

A scout vessel $P$ is positioned on the perimeter $\omega$ along the minor arc connecting Bravo and Charlie. A supply station $M$ is located exactly at the midpoint of the straight line segment $AB$. A patrol path originating from $P$ passes through station $M$ and continues until it hits the perimeter $\omega$ again at a signal tower $F$.

A command center $T$ is located at the intersection of two lines tangent to the perimeter at buoys Alpha and Bravo. A communication beam $TF$ is projected from the command center through the signal tower $F$; this beam crosses the line segment $AB$ at a relay point $K$ and exits the perimeter at a secondary sensor $L$.

In a different sector, the straight path from tower $F$ to buoy $C$ intersects the path from buoy $B$ to vessel $P$ at a coordination point $Q$. A secondary beam $TQ$ is projected from the command center through this point, intersecting the line segment $BC$ at a navigation marker $N$.

Instruments show that the distance between the command center $T$ and the sensor $L$ is exactly $25$ kilometers. Calculate the area of the triangular region formed by the relay point $K$, the supply station $M$, and the navigation marker $N$.

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
