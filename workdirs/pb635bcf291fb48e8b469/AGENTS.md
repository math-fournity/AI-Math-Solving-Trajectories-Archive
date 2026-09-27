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

In the coastal kingdom of Arcania, four navigational beacons—$A$, $B$, $C$, and $D$—are positioned along a perfectly circular shoreline defined by the Great Bay $\omega$. Two primary shipping lanes, the straight path $AC$ and the straight path $BD$, intersect at a central lighthouse $X$. 

Royal surveyors have mapped the following distances between these points:
- The distance from beacon $A$ to beacon $B$ is exactly $10$ leagues.
- The distance from beacon $A$ to beacon $D$ is exactly $24$ leagues.
- The distance from the central lighthouse $X$ to beacon $A$ is $17$ leagues.
- The distance from the central lighthouse $X$ to beacon $B$ is $21$ leagues.

A straight supply road is constructed starting at beacon $A$, running perfectly parallel to the shipping lane $BD$. This road extends in both directions, eventually intersecting the straight line passing through beacons $C$ and $D$ at a remote outpost $E$. The same road also reaches a point $Y$ on the circular shoreline of the Great Bay (where $Y$ is distinct from $A$).

The territory defined by the triangular region between the outpost $E$, the coastal point $Y$, and the beacon $D$ is to be designated as a maritime preserve. The area of this triangular region $\triangle DEY$ can be expressed as a fraction in simplest form $\frac{m}{n}$. 

Find the value of $m+n$.

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
