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

In a remote mountain range, a logistics hub is designed as a triangular zone bounded by three roads: Alpha Road ($AB$), Beta Road ($AC$), and Gamma Road ($BC$). A circular supply depot (the incircle) is positioned within this triangle such that it perfectly touches Gamma Road at a refueling station $D$, Beta Road at station $E$, and Alpha Road at station $F$.

A straight pipeline is laid from the intersection of Alpha and Beta Roads (Point $A$) to the refueling station $D$ on the far side. This pipeline enters the circular depot at one point and exits it at another; let $P$ be the exit point (the intersection furthest from $A$). 

To expand the facility, a new access road is constructed such that it is perfectly tangent to the circular depot at point $P$. This new road intersects Alpha Road at a security gate $M$ and Beta Road at a security gate $N$.

The distances between the main intersections are measured as follows:
- The total length of Alpha Road from junction $A$ to junction $B$ is 8 km.
- The total length of Beta Road from junction $A$ to junction $C$ is 10 km.
- The distance from junction $A$ to the new security gate $N$ on Beta Road is 4 km.

The distance from junction $A$ to the security gate $M$ on Alpha Road can be expressed as a simplified fraction $\frac{a}{b}$ km, where $a$ and $b$ are positive coprime integers. 

What is the value of $a+b$?

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
