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

In a specialized chemistry laboratory, a technician is organizing experimental vials on a modular rack. The rack is designed to hold rows of vials, where each vial is labeled with a distinct digit from $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$. Every available digit must be used exactly once across the ten labeled positions in the rack's configuration.

The layout of the rack consists of three rows of inputs and a final results row at the bottom:
- The first input row contains a single vial labeled $A$.
- The second input row contains a two-digit concentration represented by vials $B$ and $C$ (where $B$ is the tens digit and $C$ is the units digit).
- The third input row contains a three-digit volume represented by vials $D, E,$ and $F$ (in hundreds, tens, and units respectively).
- The final results row contains a four-digit total mass represented by vials $C, H, J,$ and $K$ (in thousands, hundreds, tens, and units respectively).

To ensure the safety of the chemical reaction, the total mass must be exactly equal to the sum of the three input values ($A + BC + DEF = CHJK$). Additionally, standard protocol dictates that the leading digit of any multi-digit number cannot be zero (specifically, $B, D,$ and $C$ cannot be $0$).

How many unique ways can the digits $0$ through $9$ be assigned to these ten specific labels to satisfy this chemical equation?

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
