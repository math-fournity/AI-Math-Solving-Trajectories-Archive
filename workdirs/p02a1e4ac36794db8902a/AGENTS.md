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

In a remote territory, three supply depots—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular network. Long-range scans confirm the straight-line distances between them are $AB = 13$ units, $BC = 15$ units, and $AC = 14$ units. A central command station ($O$) is located at the exact circumcenter of this triangular region, while a signal relay ($H$) is positioned at the orthocenter.

The territory is enclosed by a circular perimeter passing through all three depots. Two specialized communication towers are built on this perimeter: Tower $M$ is at the midpoint of the shorter arc between Bravo and Charlie, and Tower $N$ is at the midpoint of the longer arc between them.

Two patrol units, $P$ and $Q$, are stationed on the boundary roads $AB$ and $AC$, respectively. Their positions are synchronized such that the line segment $PQ$ passing through the command station $O$ is perfectly parallel to the straight line connecting depot Alpha to Tower $N$. A monitoring post ($I$) is established at a location such that the line $IP$ is perpendicular to road $AB$ and the line $IQ$ is perpendicular to road $AC$.

A drone is launched from the signal relay $H$, but it reflects off an invisible electronic barrier along line $PQ$ to a point $H'$. The straight path from this reflected point $H'$ to the monitoring post $I$ intersects the barrier $PQ$ at a specific coordination point $T$.

Analysts need to determine the ratio of the distance from Tower $M$ to point $T$ over the distance from Tower $N$ to point $T$. If this ratio $MT/NT$ is expressed in the form $\frac{\sqrt{m}}{n}$ for positive integers $m$ and $n$, where $m$ is square-free, find the value of $100m + n$.

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
