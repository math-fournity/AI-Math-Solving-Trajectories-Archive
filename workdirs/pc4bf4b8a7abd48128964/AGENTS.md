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

A specialized architectural firm is designing a triangular park defined by three landmark corner posts: the Main Arch ($A$), the Central Fountain ($B$), and the Clock Tower ($C$). The boundary paths $AB$, $BC$, and $AC$ form a right-angled layout where the internal angle at the Main Arch is $20^\circ$ and the angle at the Clock Tower is $70^\circ$. A security surveillance hub ($O$) is located at the exact center of the park's circumscribed circle.

Two specialized light fixtures, $D$ and $E$, are positioned along the straight path $AC$ connecting the Main Arch and the Clock Tower. Their positions are determined by specific sightlines from the Central Fountain ($B$):
1. The line of sight from the Fountain to the security hub ($BO$) exactly bisects the angle formed between the path to the Main Arch and the path to light fixture $D$ ($\angle ABD$).
2. The path from the Fountain to light fixture $E$ ($BE$) exactly bisects the angle formed between the path to the Clock Tower and the path to light fixture $D$ ($\angle CBD$).

To ensure proper drainage, two straight underground pipes, $DP$ and $EQ$, are laid out. Both pipes start from their respective light fixtures on path $AC$ and run perfectly perpendicular to path $AC$ until they intersect the line extending from the path $BC$ at drainage connection points $P$ and $Q$.

A surveyor stands at the Main Arch ($A$) and measures the angle between the lines of sight to the two drainage connection points $P$ and $Q$. What is the measure of $\angle PAQ$ in degrees?

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
