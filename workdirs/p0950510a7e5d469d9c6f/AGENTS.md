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

In a remote industrial complex, a specialized storage bunker is constructed in the shape of a pyramid named $A B C E H$, where $H$ is the apex. The foundation of the bunker is a convex quadrilateral floor $A B C E$. A reinforcement beam $B E$ runs across the floor, dividing it into two zones—triangle $A B E$ and triangle $B C E$—which have exactly the same floor area.

Technical specifications for the bunker's structural ribs are as follows:
- The length of the steel rib $A B$ is exactly 1 unit.
- The two external boundary ribs $B C$ and $C E$ are fabricated to be equal in length.
- Two support cables, $A H$ and $E H$, connect the apex to the foundation; the combined length of these two cables ($A H + E H$) is $\sqrt{2}$ units.

The total interior capacity (volume) of the bunker is exactly $1/6$ cubic units.

A safety inspector needs to install a spherical gas sensor inside the bunker. To maximize the sensor's coverage, they must select a sphere with the largest possible volume that can be contained entirely within the pyramid $A B C E H$. 

Find the radius of this largest possible sphere.

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
