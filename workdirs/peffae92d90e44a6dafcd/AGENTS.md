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

A specialized architectural firm is designing a futuristic modular laboratory. The structure is shaped like a vertical regular hexagonal prism with a total interior volume of $V$. The floor of the laboratory is defined by its six corners, $A, B, C, D, E$, and $F$. The center point of this floor is designated as $O$, while the center point of the ceiling is $O_1$.

On the ceiling, six support anchors—$M, N, P, Q, R$, and $S$—are installed exactly at the midpoints of the six boundary edges of the hexagonal roof.

The design calls for two intersecting light-sculptures made of laser beams:
1. The first is a hexagonal pyramid formed by connecting the ceiling center $O_1$ to each of the floor corners $A, B, C, D, E$, and $F$.
2. The second is a hexagonal pyramid formed by connecting the floor center $O$ to each of the ceiling anchors $M, N, P, Q, R$, and $S$.

To ensure the safety of the researchers, the central zone where these two laser pyramids overlap must be strictly climate-controlled. Calculate the volume of this common intersection region in terms of the total prism volume $V$.

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
