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

In the city of Aetheria, there is a set of active power substations, and a group of industrial factories must connect to them to draw energy. Each factory $i$ requires a specific positive amount of energy, $e_i$ kilowatts.

When a factory connects to a substation, it incurs an "Operating Stress" equal to the product of its own energy requirement $e_i$ and the "Total Load" of that substation (the sum of energy requirements of all factories connected to it). The "Total Grid Strain" is defined as the sum of the Operating Stresses of all factories in the city.

Initially, the factory owners reach a "Nash Equilibrium" configuration: a state where no individual factory owner can reduce their own Operating Stress by unilaterally switching their connection to a different substation. In this equilibrium state, the Total Grid Strain is calculated to be $M_1$.

A veteran grid engineer later proposes an alternative assignment of factories to substations (not necessarily an equilibrium) that results in a Total Grid Strain of $M_2$.

Considering all possible positive integer counts of substations and all possible positive energy requirements for the factories, what is the maximum possible value of the ratio $M_1/M_2$?

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
