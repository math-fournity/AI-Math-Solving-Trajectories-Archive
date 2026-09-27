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

In a remote territory, three survey outposts—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a large triangular perimeter. To improve communications, a supply road is built between Alpha and Bravo. Two relay stations, Delta ($D$) and Echo ($E$), are placed on this road such that the road is divided into three perfectly equal segments: $AD$, $DE$, and $EB$. Simultaneously, a mid-way checkpoint, Fox ($F$), is established exactly halfway along the road connecting Alpha and Charlie.

Three distinct logistics paths are then mapped out:
1. A path from Delta to Fox ($DF$).
2. A path from Bravo to Fox ($BF$).
3. A path from Charlie to Echo ($CE$).

The path from Charlie to Echo intersects the Delta-Fox path at a point designated as junction Gamma ($G$). Further along, the Charlie-Echo path intersects the Bravo-Fox path at a point designated as junction Hotel ($H$).

A specialized drone survey calculates that the area of the triangular region bounded by the stations Delta and Echo and the junction Gamma ($DEG$) is exactly 18 square kilometers.

Calculate the area of the triangular region bounded by the checkpoint Fox and the two junctions Gamma and Hotel ($FGH$). If the area is expressed as an irreducible fraction $\frac{a}{b}$, what is the value of $a + b$?

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
