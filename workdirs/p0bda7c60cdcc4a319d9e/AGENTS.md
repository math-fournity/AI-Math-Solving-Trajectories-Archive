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

In the competitive world of architectural acoustics, a designer is planning the layout of a concert hall defined by a central triangular stage area, $ABC$. The primary acoustic focus is determined by the angle at the main podium, $A$. Measurements confirm that $\sin \angle A = \frac{4}{5}$ and that this angle is acute.

To optimize sound projection, a specialized microphone array is positioned at point $D$, which is located outside the stage area. This position is chosen such that the line of sight $AD$ perfectly bisects the angle $\angle BAC$. The microphone array at $D$ is specifically configured so that the angle formed between the paths to the two side corners of the stage, $\angle BDC$, is exactly $90^\circ$.

The precision-calibrated distance from the podium $A$ to the microphone $D$ is exactly $1$ unit. Furthermore, the ratio of the distance from the microphone to the left corner $B$ compared to the right corner $C$ is exactly $3:2$ (i.e., $\frac{BD}{CD} = \frac{3}{2}$).

The total length of the two side boundaries of the stage, $AB + AC$, can be expressed in the simplified form $\frac{a\sqrt{b}}{c}$, where $a, b,$ and $c$ are pairwise relatively prime positive integers. Find the value of $a + b + c$.

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
