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

In a remote mountain range, a specialized irrigation system is designed in the shape of a large triangular terrace field, denoted by $ABC$. The boundary $AB$ is a stone wall exactly equal in length to the irrigation canal $BC$. At the heart of this field lies a circular reservoir $\omega$, which is perfectly tangent to all three boundaries $AB$, $BC$, and $AC$.

A maintenance path $PQ$ is constructed such that $P$ lies on the stone wall $AB$ and $Q$ lies on the boundary $AC$. This path $PQ$ is perfectly parallel to the irrigation canal $BC$ and runs exactly along the edge of the circular reservoir $\omega$, touching it at a single point.

A surveyor marks a point $M$ exactly at the halfway point of the canal $BC$. To ensure proper drainage, a sensor is placed at $M$ and linked to $Q$ and $P$. The alignment is such that the angle formed between the boundary $AC$ and the line $QM$ (angle $CQM$) is identical to the angle formed between the maintenance path $PQ$ and the line $QM$ (angle $PQM$).

If the distance along the boundary from the peak corner $A$ to the path junction $Q$ is measured to be $1$ unit, determine the total length of the perimeter of the triangular field $ABC$.

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
