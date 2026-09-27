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

In a remote sector of the galaxy, a specialized solar sail called the "L-Unit" is being deployed between two fixed anchor beacons, Station Alpha ($A$) and Station Beta ($B$). These stations are positioned relative to a central command hub, Vertex Control ($V$).

The spatial coordinates are fixed such that the angle formed at the command hub between the two stations, $\angle AVB$, is exactly $75^\circ$. Navigation sensors report that the distance from the hub to Station Alpha ($AV$) is $\sqrt{2}$ units, while the distance to Station Beta ($BV$) is $\sqrt{3}$ units.

The L-Unit sail is a "lune" structure—a flat region defined by two circular arcs that meet precisely at endpoints $A$ and $B$. To avoid interference with the communication beams (the infinite lines $\overleftrightarrow{VA}$ and $\overleftrightarrow{VB}$), the sail must be designed such that it does not touch or cross these lines at any point other than its connection ports at $A$ and $B$.

Engineers aim to maximize the surface area of this sail while adhering to these boundary constraints. Let $k$ represent the area of the largest possible lune $L$ that satisfies these conditions.

Calculate the value of:
\[ \frac{k}{(1+\sqrt{3})^2} \]

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
