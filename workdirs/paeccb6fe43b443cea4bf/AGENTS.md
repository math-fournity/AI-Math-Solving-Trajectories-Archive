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

In a remote desert, a state-of-the-art research outpost is built in the shape of a perfect regular tetrahedron with a side length of exactly 1 kilometer. The four vertices of the outpost are designated as North Base ($A$), West Base ($B$), South Base ($C$), and the Peak ($D$).

A specialized fiber-optic sensor cable is being installed around the structure, passing through four specific checkpoints located on the edges of the outpost:

1.  **Checkpoint Alpha ($E$):** Located on the structural beam connecting the North Base and West Base ($AB$), positioned precisely $2/3$ km from the North Base ($A$).
2.  **Checkpoint Beta ($F$):** Located on the beam connecting the West Base and South Base ($BC$), positioned precisely $3/4$ km from the West Base ($B$).
3.  **Checkpoint Gamma ($G$):** Located on the beam connecting the South Base and the Peak ($CD$), positioned exactly $1/2$ km from the South Base ($C$).
4.  **Checkpoint Delta ($H$):** This checkpoint is located at the intersection of the structural beam connecting the North Base and the Peak ($AD$) and the unique flat plane defined by the positions of Checkpoints Alpha, Beta, and Gamma.

A maintenance technician must calculate the total length of the triangular perimeter formed by connecting Checkpoint Delta to Checkpoint Alpha, Checkpoint Alpha to Checkpoint Gamma, and Checkpoint Gamma back to Checkpoint Delta (the perimeter of triangle $HEG$).

The total length of this path can be expressed in the simplified form $\frac{\sqrt{a}}{b} + \frac{c\sqrt{d}}{e} + \frac{\sqrt{f}}{g}$ kilometers, where $a, b, c, d, e, f, g$ are positive integers, the fractions are in simplest form, and the radicals are square-free. 

Find the value of $a+b+c+d+e+f+g$.

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
