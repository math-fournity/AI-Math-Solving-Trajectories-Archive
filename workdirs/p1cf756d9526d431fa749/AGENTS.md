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

In the competitive world of architectural acoustics, a design firm is testing a specific class of "Acoustic Zones" shaped like non-isosceles triangles $ABC$. These zones are engineered such that the squared lengths of the two side walls, $AC$ and $BC$, always sum to exactly twice the square of the front boundary wall, $AB$ (i.e., $AC^2 + BC^2 = 2 AB^2$).

To optimize sound distribution, two calibration markers are placed on the front wall $AB$:
1. A central sensor $M$ is positioned exactly at the midpoint of $AB$.
2. A focal point $D$ is positioned on $AB$ such that the line of sight $CD$ perfectly bisects the interior angle at corner $C$.

For advanced spatial audio, a specialized transmitter $E$ is installed in the room's floor plane. Its location is precisely calculated so that the focal point $D$ serves as the mathematical incenter of the triangle formed by the transmitter $E$, the central sensor $M$, and the corner $C$ (triangle $CEM$).

As the dimensions of the Acoustic Zone $ABC$ vary while maintaining the core architectural constraint ($AC^2 + BC^2 = 2 AB^2$), it has been observed that exactly one of the following three ratios of distances remains invariant across all possible configurations:
\[ \frac{CE}{EM}, \quad \frac{EM}{MC}, \quad \frac{MC}{CE} \]

Find the value of this constant ratio.

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
