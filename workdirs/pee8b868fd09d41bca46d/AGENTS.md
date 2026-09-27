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

In the architectural planning of a new waterfront district, a surveyor is mapping out a quadrilateral plot of land designated as $ABCD$. To ensure the aesthetic symmetry of the district, the head architect has stipulated two specific angular constraints for the plot: the internal angle at the northwest corner, $\angle BAD$, must be exactly equal to the internal angle at the northeast corner, $\angle ADC$. Furthermore, the angle formed by the sightline from the northwest corner to the southeast corner, $\angle ABD$, must be identical to the angle formed at the southeast corner between the southern and western boundaries, $\angle BCD$.

The surveying team has measured three of the primary distances:
- The western boundary, $AB$, measures exactly 8 decameters.
- The diagonal distance from the northwest corner to the southeast corner, $BD$, measures 10 decameters.
- The southern boundary, $BC$, measures 6 decameters.

The length of the eastern boundary, $CD$, is calculated to be a rational number in simplest form $m/n$, where $m$ and $n$ are relatively prime positive integers. Find the value of $m + n$.

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
