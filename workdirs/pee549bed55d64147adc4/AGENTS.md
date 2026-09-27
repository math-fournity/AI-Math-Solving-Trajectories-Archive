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

A specialized deep-sea research station is located at position $A$ on the perimeter of a circular bay, denoted as $\omega$. Two underwater communication relays are positioned at points $B$ and $C$ on the same perimeter. The distance between the station $A$ and relay $B$ is exactly 5 nautical miles, the distance between relays $B$ and $C$ is 7 nautical miles, and the distance between station $A$ and relay $C$ is 3 nautical miles.

An automated submarine travels along a straight-line path from station $A$ that perfectly bisects the angle formed by the paths $AB$ and $AC$. This submarine path intersects the straight-line cable connecting $B$ and $C$ at a point $D$, and eventually reaches the far side of the bay's perimeter at point $E$.

Engineers establish a circular sensor range, $\gamma$, using the segment $DE$ as its diameter. This sensor range $\gamma$ intersects the bay's perimeter $\omega$ at two points: the submarine's destination $E$ and a specific monitoring point $F$.

The researchers need to calculate the squared distance between the research station $A$ and the monitoring point $F$. If this value is expressed as a simplified fraction $AF^2 = \frac{m}{n}$ where $m$ and $n$ are relatively prime positive integers, find the value of $m + n$.

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
