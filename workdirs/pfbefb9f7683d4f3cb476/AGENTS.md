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

In a remote industrial complex, engineers have constructed a specialized storage facility. The base of the facility is a massive cubic structure, $ABCD-A'B'C'D'$, where the floor is the square $A'B'C'D'$ and the ceiling is the square $ABCD$. Every edge of this cube measures exactly 6 units. Bolted directly onto the ceiling $ABCD$ is a pyramid-shaped roof with apex $E$, such that $E$ sits above the cube. Every edge of this pyramid, including the four edges meeting at $E$ and the four edges of the square base $ABCD$, also measures exactly 6 units.

A robotic sensor is mounted at point $G$, located at the exact centroid of the triangular roof face $ABE$. The sensor needs to be moved to a data port located at vertex $D'$ on the floor of the cubic structure. The sensor must be moved along the exterior surface of the combined structure (the four triangular faces of the roof and the four vertical square faces of the cube). It cannot pass through the interior of the structures or across the base $A'B'C'D'$.

What is the length of the shortest path the sensor can take from point $G$ to point $D'$ along the surface? Write your answer in the form $\sqrt{a+b \sqrt{3}}$, where $a$ and $b$ are positive integers.

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
