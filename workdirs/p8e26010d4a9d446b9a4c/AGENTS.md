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

An architect is designing a specialized modern art installation consisting of a heavy structural node suspended by four high-tension steel cables. The installation is anchored to four points in a gallery space: three points $A$, $B$, and $C$ are located on the flat, horizontal floor, while the fourth point $D$ is a floating junction box in the air.

The structural requirements dictate a perfectly isosceles-tetrahedral symmetry for the cable lengths. The cable connecting floor point $A$ to floor point $B$ and the cable connecting floor point $C$ to the junction $D$ both measure exactly $\sqrt{13}$ meters. The cable connecting floor point $A$ to the junction $D$ and the cable connecting floor points $B$ and $C$ both measure exactly $\sqrt{20}$ meters. Finally, the cable connecting floor point $A$ to floor point $C$ and the cable connecting floor point $B$ to the junction $D$ both measure exactly $\sqrt{15}$ meters.

To ensure the safety of the installation, the lead engineer must calculate the vertical clearance of the junction. Specifically, if $h$ represents the perpendicular vertical distance from the junction $D$ to the level floor plane defined by $A$, $B$, and $C$, calculate the value of $h^2$.

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
