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

In a remote territory, a communications network is defined by three primary transmission towers—Tower A, Tower B, and Tower C—which form an acute triangle. All three towers receive signals from a central orbital satellite, whose circular coverage zone, Boundary $\Gamma$, passes exactly through the locations of A, B, and C.

A straight maintenance road connects Tower B and Tower C. A specialized directional signal is broadcast from Tower A, exactly bisecting the interior angle formed by the paths to B and C. This signal path crosses the road $BC$ at a relay station, Point E, and continues until it hits the edge of the satellite’s coverage zone at Point N.

The satellite’s orbit has a designated "Reference Point" $A'$, located on the Boundary $\Gamma$ at the position diametrically opposite to Tower A. A straight fiber-optic cable connects Tower A to Point $A'$. This cable intersects the road $BC$ at a junction box, Point V.

Technicians have recorded the following ground distances:
- The distance between relay station E and junction box V is 6 units.
- The distance from junction box V to the orbital Reference Point $A'$ is 7 units.
- The straight-line distance from the Reference Point $A'$ to the signal edge Point N is 9 units.

Based on these measurements, calculate the radius of the satellite's circular coverage zone $\Gamma$. If the radius is expressed as an irreducible fraction $\frac{a}{b}$, find the value of $a + b$.

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
