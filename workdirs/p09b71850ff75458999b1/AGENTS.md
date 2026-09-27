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

In a futuristic circular space station, there are 50 docking bays arranged at equal intervals along the outer hull, forming a perfect 50-sided perimeter. The station’s central hub can be reconfigured by installing internal pressurized corridors (diagonals) that connect any two docking bays, provided these corridors do not cross one another. 

The station’s logistics AI needs to ensure that at least one corridor in any possible full reconfiguration (a complete triangulation of the station) will partition the outer hull into two distinct sectors. Each sector is measured by the number of docking bays along its outer edge. 

The AI is programmed with two target sector sizes, $a$ and $b$. The safety protocol requires that for any possible internal corridor layout, there must exist at least one corridor such that both sectors it creates have an edge length equal to either $a$ or $b$. 

To maintain maximum flexibility in choosing these targets, the AI must minimize the discrepancy between the two values, defined as the absolute difference $|a - b|$.

Find the smallest integer $n$ such that there exist two target sizes $a$ and $b$ with $|a - b| \le n$, ensuring that every possible full internal corridor layout contains at least one corridor that splits the 50-bay perimeter into two parts, each having a length of exactly $a$ or $b$ bays.

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
