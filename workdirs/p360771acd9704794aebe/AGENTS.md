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

A specialized laser-guided excavation system is being tested on a triangular plot of land defined by three markers: Alpha ($A$), Bravo ($B$), and Charlie ($C$). The boundary lines between the markers are perfectly straight, and the path from Alpha to Charlie meets the path from Alpha to Bravo at a precise $90^\circ$ angle. A surveyor at marker Bravo determines that the angle between the paths leading to Alpha and Charlie is exactly $20^\circ$.

A technician installs a signal emitter at point $E$, which is located on the boundary line between Alpha and Charlie. This emitter is positioned such that the line of sight from Bravo to $E$ perfectly bisects the $20^\circ$ angle at marker Bravo.

Simultaneously, a remote sensor is placed at point $F$ along the boundary line between Alpha and Bravo. A measurement taken from marker Charlie reveals that the angle between the line of sight to Alpha and the line of sight to the sensor at $F$ is exactly $30^\circ$.

The engineering team needs to calibrate the alignment between the sensor at $F$ and the emitter at $E$. Calculate the measure of the angle formed between the line of sight from $F$ to Charlie and the line of sight from $F$ to $E$ (expressed in degrees).

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
